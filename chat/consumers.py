import json 
import ollama
import markdown2
import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Project, ChatMessage
from asgiref.sync import sync_to_sync

User = get_user_model


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        self.room_group_name = f'{self.project_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, code):
            await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
         data = json.loads(text_data)
         user_message = data.get('message')

         await self.send(text_data=json.dumps({
              'message' : user_message, 'sender': "user"
         }))

         project = await self.get_project()

         if not project:
              return
         
         ai_response = ""
         raw_markdown_response = ""
         stream = ollama.chat(
              model = 'deepseek-r1:1.5b',
              message=[{"role": "user", "content": user_message}],
              stream= True
         )
         
         for chunk in stream:
              raw_markdown_response += chunk['message']['content']
              formatted_html = markdown2.markdown(raw_markdown_response)

              #send all chuck imediatly to the frontend
              await self.send(text_data=json.dumps({
                   'formatted_html': formatted_html,
                   'sender': 'ai'
                   
                   
              }))

              await asyncio.sleep(0.5)

              #save database 
              await self.save_message(project, self.scop['user'], user_message, formatted_html)

              #close websote connection
              await self.send(text_data=json.dumps({
                   'close': 'True',
                   
              }))

              await self.close()

              


    
        
        

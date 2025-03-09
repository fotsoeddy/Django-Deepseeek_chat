Django DeepSeek Chat
📌 Description
Django DeepSeek Chat is a real-time chat application built with Django, Django Channels, and WebSockets. It allows users to create and join dynamic chat rooms and interact with an integrated DeepSeek AI. The application is optimized for a smooth and responsive experience, enabling users to ask questions to the AI, learn, and collaborate on projects.

🚀 Features
📡 WebSockets with Django Channels for real-time communication

👤 User authentication (login and registration)

💬 Dynamic chat rooms (creation and management)

🔄 Real-time messaging system with instant updates

🤖 DeepSeek AI integration for answering questions and user assistance

📝 Message storage in database

🎨 Responsive UI with Bootstrap

☁️ Deployment with Daphne and Redis

🛠 Prerequisites
Before starting, ensure you have the following installed:

Python 3.8+

pip and virtualenv

PostgreSQL or SQLite (database choice)

Redis (for WebSocket management)

Ollama installed locally

DeepSeek model configured locally with Ollama



📦 Installation
🔹 1. Clone the repository

git clone https://github.com/fotsoeddy/Django-Deepseeek_chat.git
cd Django-Deepseeek_chat
🔹 2. Create and activate virtual environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
🔹 3. Install dependencies

pip install -r requirements.txt
🔹 4. Configure database

python manage.py migrate
🔹 5. Create superuser (optional for admin)

python manage.py createsuperuser
🔹 6. Start development server

python manage.py runserver
Access the application at http://127.0.0.1:8000

⚙️ WebSocket Configuration with Daphne and Redis
To run the server in WebSocket mode with Daphne and Redis:

daphne -b 0.0.0.0 -p 8000 deepseek_chat.asgi:application
If using Redis as channels backend, ensure it's installed and running:

redis-server
📜 .env File (Environment Configuration Example)
Create a .env file at project root with these configurations:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/deepseek_chat
REDIS_URL=redis://127.0.0.1:6379/0
🏗 Technologies Used
Django (core backend)

Django Channels (WebSocket handling)

Redis (real-time message broker)

Daphne (ASGI server)

PostgreSQL/SQLite (database)

Tailwinds (responsive UI)

Ollama (local DeepSeek model execution)

🎯 Roadmap
🔜 Real-time notifications

🔜 Advanced multi-room support

🔜 Searchable conversation history

🔜 AI interaction improvements

🤝 Contributing
Contributions are welcome! To contribute:

Fork the project 🍴

Create a feature branch (git checkout -b feature-xyz)

Commit changes (git commit -m "Add new feature")

Push branch (git push origin feature-xyz)

Create Pull Request 🛠

💬 Contact
Developed by Fotso Eddy.

🌐 Portfolio https://fotsoeddysteve.vercel.app/

📧 Email: fotsotachulaeddysteve@gmail.com

🐙 GitHub


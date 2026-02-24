# Conversational-AI-Chatbot-using-LangChain-Groq-LLaMA-3.1-
A Python-based conversational AI chatbot built with LangChain and Groq's LLaMA 3.1 model, featuring memory handling, personality-based responses, and manual chat history management.


🤖 Conversational AI Chatbot using LangChain & Groq

This project is a command-line conversational chatbot built using:

LangChain

Groq LLM (LLaMA 3.1)

Python

Manual memory management

The chatbot maintains conversation history, has a friendly personality, and supports chat control commands like exit and clear.

🚀 Features

✅ Uses Groq LLaMA 3.1 model

✅ Friendly & slightly humorous AI personality

✅ Maintains conversation memory (last 5 interactions)

✅ Manual memory trimming (no built-in memory class)

✅ Handles empty input safely

✅ exit command to quit chatbot

✅ clear command to reset chat history

✅ Built using LangChain Expression Language (LCEL)

🧠 How Memory Works

Chat history is stored manually in a Python list.

Both user and AI messages are appended.

Memory is limited to last 10 messages (5 user + 5 AI).

chat_history = chat_history[-10:]

This ensures controlled memory usage and realistic conversational behavior.

🛠 Technologies Used

Python

LangChain

Groq API

dotenv

Main components used:

ChatGroq

ChatPromptTemplate

MessagesPlaceholder

StrOutputParser

HumanMessage

AIMessage

⚙ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
2️⃣ Install dependencies
pip install langchain langchain-groq python-dotenv
3️⃣ Add your Groq API key

Create a .env file:

GROQ_API_KEY=your_api_key_here
▶ How to Run
python chatbot.py
💬 Commands
Command	Function
exit	Exit the chatbot
clear	Clears chat history
(empty input)	Prompts user to enter valid text
📂 Project Structure
├── chatbot.py
├── .env
├── README.md
📌 Example Interaction
Ask your question: Hi
AI Message: Hello! 😊 How can I help you today?

Ask your question: My name is Kashif
AI Message: Nice to meet you, Kashif!

Ask your question: What is my name?
AI Message: Your name is Kashif.

🎯 Learning Objectives

This project demonstrates:

Working with LLM APIs

Prompt engineering

Manual conversation memory management

LCEL chaining in LangChain

Environment variable handling

CLI-based AI applications

🔮 Future Improvements

Convert into web app (Flask / FastAPI)

Add persistent database memory

Add streaming responses

Add multi-user support

Deploy on cloud

👨‍💻 Author

Kashif Manzoor
Python Developer | AI Enthusiast

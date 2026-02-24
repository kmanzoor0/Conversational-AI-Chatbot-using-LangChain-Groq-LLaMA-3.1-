from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model_name = 'llama-3.1-8b-instant')

chat_history = []

prompt = ChatPromptTemplate.from_messages([
    ('system','You are a friendly and slightly humorous AI assistant.'),
    MessagesPlaceholder(variable_name ="chat_history"),
    ('human','{question}')
])
parser = StrOutputParser()
chain = prompt |model | parser

while True:
    user_input = input('Ask your question : ')
    if user_input.strip().lower() == 'exit':
        print('GoodBye')
        break
    elif user_input == '':
        print('Bot : Please Type Something so i can assist you')
        continue
    elif user_input.strip().lower() == 'clear':
        chat_history = []
        print('Bot : Chat history cleared ')
        continue
    result = chain.invoke({
        "chat_history":chat_history,
        "question":user_input
        })
    print('AI Message :',result)
    chat_history.append(HumanMessage(content = user_input))
    chat_history.append(AIMessage(content = result))
    chat_history = chat_history[-10:]

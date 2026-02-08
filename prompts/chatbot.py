from langchain_groq import ChatGroq 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv 

load_dotenv()


model = ChatGroq(
  model="groq/compound-mini", 
  max_tokens=200, 
  temperature=1.5
)


chat_history = [
  SystemMessage(content='Your are helpful ai assistant')
]


while True: 
  user_input = input("You: ")
  chat_history.append(HumanMessage(content=user_input))
  
  if user_input == "exit": 
    break 
  
  result = model.invoke(chat_history)
  chat_history.append(AIMessage(result.content)) 

  print("AI: ", result.content)

print(chat_history)

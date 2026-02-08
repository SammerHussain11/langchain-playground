from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq 
from dotenv import load_dotenv 

load_dotenv()

model = ChatGroq(
  model="groq/compound-mini", 
  max_tokens=200, 
  temperature=1.5
)

messages = [
  SystemMessage("You are a helpfull assistant"), 
  HumanMessage("Tell me about agentic ai")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

response = model.invoke("Hello , LangChain! Explain yourself in one sentence. ")
print(response.content)
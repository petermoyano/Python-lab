# This is Hello World App, from Langchain's Mendable ai helper bot. 
from langchain import OpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os



load_dotenv()

API_KEY= os.getenv("OPENAI_API_KEY")
API_KEY2= os.environ['OPENAI_API_KEY']


print("from getenv", API_KEY)
print("from environ", API_KEY2)

llm= OpenAI(model="gpt3.5-turbo",  temperature=0)

chain=ConversationChain(llm=llm)

response= chain.predict(prompt="Hello World!")

print(response)

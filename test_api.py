import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()
llm = ChatOpenAI(model=os.getenv("DEFAULT_MODEL"))
print(llm.invoke("Xin chào?").content)
from langchain_google_genai import ChatGoogleGenerativeAI
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             google_api_key=GEMINI_API_KEY)

question = input("Enter the question")
response = llm.invoke(question)
print(response.content)
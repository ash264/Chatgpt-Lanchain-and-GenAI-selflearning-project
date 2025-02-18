import os
from langchain_openai import OpenAIEmbeddings

import httpx

llm=OpenAIEmbeddings(model="gte-large", api_key=os.getenv("DEV_GENAI_API_KEY"), base_url='https://genai-api-dev.dell.com/v1', http_client=httpx.Client(verify=False))
#gte-large, bge-base-en-v1-5, bge-large-en-v1-5
text = input("Enter the text")
response = llm.embed_query(text)
print(response)
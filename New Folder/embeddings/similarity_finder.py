import os
from langchain_openai import OpenAIEmbeddings
import numpy as np

import httpx

llm=OpenAIEmbeddings(model="gte-large", api_key=os.getenv("DEV_GENAI_API_KEY"), base_url='https://genai-api-dev.dell.com/v1', http_client=httpx.Client(verify=False))
#gte-large, bge-base-en-v1-5

text1 = input("Enter the text1")
text2 = input("Enter the text2")
response1 = llm.embed_query(text1)
response2 = llm.embed_query(text2)

similarity_score = np.dot(response1,response2)

print(similarity_score*100,'%')
import os
from langchain_openai import OpenAIEmbeddings
import numpy as np

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

input1 = input("Enter First Input")
input2 = input("Enter Second Input")

response1 = embeddings.embed_query(input1)
response2 = embeddings.embed_query(input2)
print(response1)
similarity_score = np.dot(response1,response2)

print(similarity_score*100,'%')
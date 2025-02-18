import os
from langchain_community.chat_models import ChatOllama
import httpx

llm = ChatOllama(
    model="gemma:2b",
    # temperature=0,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
    # api_key=os.getenv("DEV_GENAI_API_KEY"),
    # base_url='https://genai-api-dev.dell.com/v1',
    # http_client=httpx.Client(verify=False),
)
question = " What is the capital of India? Answer in 5 words"
response = llm.invoke(question).content 
print(response)

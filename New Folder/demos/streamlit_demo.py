import httpx
import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug

set_debug(True)

llm = ChatOpenAI(
    model="mixtral-8x7b-instruct-v01",
    # temperature=0,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
    api_key=os.getenv("DEV_GENAI_API_KEY"),
    base_url='https://genai-api-dev.dell.com/v1',
    http_client=httpx.Client(verify=False),
)

st.title("Get LLM response here")

question = st.text_input("Ask your prompt")

if question:
    response = llm.invoke(question).content 
    st.write(response)

# print(response)

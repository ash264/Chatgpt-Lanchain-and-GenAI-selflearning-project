import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate

import httpx

llm=ChatOpenAI(model="mixtral-8x7b-instruct-v01", api_key=os.getenv("DEV_GENAI_API_KEY"), base_url='https://genai-api-dev.dell.com/v1', http_client=httpx.Client(verify=False))

prompt_template = ChatPromptTemplate.from_messages(
[
    ("system","You are a Agile Coach.Answer any questions "
              "related to the agile process"),
    ("human", "{input}")
]
)

st.title("Agile Guide")

input = st.text_input("Enter the question:")

chain = prompt_template | llm

if input:
    response = chain.invoke({"input":input})
    st.write(response.content)
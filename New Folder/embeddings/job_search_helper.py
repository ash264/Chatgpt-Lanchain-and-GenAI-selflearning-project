import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
# Alternative to Chrome can be FAISS

import httpx

llm=OpenAIEmbeddings(model="gte-large", api_key=os.getenv("DEV_GENAI_API_KEY"), base_url='https://genai-api-dev.dell.com/v1', http_client=httpx.Client(verify=False))
#gte-large, bge-base-en-v1-5, bge-large-en-v1-5

document = TextLoader("job_listings.txt").load()
text_splitter= RecursiveCharacterTextSplitter(chunk_size=200,
                                              chunk_overlap=10)
chunks=text_splitter.split_documents(document)
db=Chroma.from_documents(chunks,llm)
retriever = db.as_retriever()

text = input("Enter the query")

docs = retriever.invoke(text) # similarity search

for doc in docs:
    print(doc.page_content)
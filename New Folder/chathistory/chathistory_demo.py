import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

import httpx

llm=ChatOpenAI(model="mixtral-8x7b-instruct-v01", api_key=os.getenv("DEV_GENAI_API_KEY"), base_url='https://genai-api-dev.dell.com/v1', http_client=httpx.Client(verify=False))

prompt_template = ChatPromptTemplate.from_messages(
[
    ("system", "You are a Agile Coach.Answer any questions "
               "related to the agile process"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
]
)

chain = prompt_template | llm

history_for_chain = ChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)

print("Agile Guide")

while True:
    question = input("Enter the question:")
    if question:
        response = (chain_with_history
                    .invoke({"input": question},
                            {"configurable":{
                                "session_id":"abc123"
                            }}))
        print(response.content)

        
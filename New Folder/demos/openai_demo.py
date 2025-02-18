import os
# from langchain_openai import ChatOpenAI
from openai import OpenAI
import httpx

# available_models = ["mixtral-8x7b-instruct-v01", "llamaguard-7b", "mistral-7b-instruct-v03", "phi-3-mini-128k-instruct", "llama-3-8b-instruct", "llama-3-1-8b-instruct", "codellama-13b-instruct", "sqlcoder-7b-2", "codestral-22b-v0-1"]

# Initialize OpenAI client
client = OpenAI(
    base_url='https://genai-api-dev.dell.com/v1',
    http_client=httpx.Client(verify=False),
    api_key=os.getenv("DEV_GENAI_API_KEY") # OPENAI_API_KEY, DEV_GENAI_API_KEY
)
question = "What is sun?"
# Function to get response from the API
completion = client.completions.create(
        model="llama-3-8b-instruct",
        max_tokens=100,
        prompt=question
    )
response = completion.choices[0].text
print(response)




# from openai import OpenAI
# client = OpenAI()

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )

# print(response.choices[0].message.content)
from langchain.llms import OpenAI

import httpx

# response = httpx.get('https://example.com', verify=False)  # Disable SSL Verification (Not Recommended)

print("Hi")

api_key = 'sk-cYcZX4dzTQy2vE8m2-HY5fZJ_OW5kVYVvSR-1LNympT3BlbkFJhI03hxWIQM9gD1ul1bKwWoSYcweZqlOKcNVP7TcH0A'

llm = OpenAI(
    openai_api_key=api_key,
) # openai.APIConnectionError: Connection error ---> At home try with home internet

result = llm("Write short poem")

print(result)
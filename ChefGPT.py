import os
import openai


key = open('apikey.txt', 'r')
openai.api_key= os.getenv(key.readline)

response {"role": "system", "content": "You are a helpful assistant."}
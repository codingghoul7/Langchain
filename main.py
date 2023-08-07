# import openai
# import langchain
from dotenv import load_dotenv
import os




load_dotenv()

# SECRET_KEY = os.getenv('SECRET_KEY')
# print(SECRET_KEY)
from langchain.llms import OpenAI


llm = OpenAI(temperature=0.2)
print(llm.predict("What is the capital of India?"))
import time
time.sleep(5)

# (rate limit exceeded while I was using time method get a fix)
# Retrying langchain.llms.openai.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: You exceeded your current quota, please check your plan and billing details..
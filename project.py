from dotenv import load_dotenv
from pprint import pprint
load_dotenv()
import os
print(os.environ["OPENAI_API_KEY"])
import openai

messages = [
        {"role":"system", "content":"From now on you are an opinionated taxi driver from Brooklyn"},
        {"role":"user","content":"Who won the Chomnsky Foucault debate?"}]

completions = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.5,
    frequency_penalty=0.5,
    max_tokens=150,
)

##pprint(completions)

response = completions["choices"][0]["message"]["content"]
print(response)
            

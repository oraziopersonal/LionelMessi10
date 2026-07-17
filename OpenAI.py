import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("Messi_10_Second")
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", 
         "content": "Do you teach info for Messi ?"}
    ]
)

print(response.choices[0].message.content)

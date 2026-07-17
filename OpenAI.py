from openai import OpenAI

client = OpenAI(
    api_key="Messi_10_Winner_2022"
)

response = client.chat.completions.create(
    model="gpt-5o-mini",
    messages=[
        {"role": "Do you know only footballer Lionel Messi ", 
         "content": "Messi is the best football player more to Pelè ? "}
    ]
)

print(response.choices[0].message.content)

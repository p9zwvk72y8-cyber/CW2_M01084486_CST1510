from openai import OpenAI

client =OpenAI( "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")

prompt = 'Hello,How are you doing'
completion = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role":"developer","content": "You are a helpful assistant."},
        {"role":"user","content":prompt}
    ]
)
print(completion.choices[0].message.comtent)
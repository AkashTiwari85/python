import openai
openai.api_key='YOUR_API_KEY'
messages=[{"role": "system","content":
           "you are a intelligent"
          "assistant."}]
while True:
    message=input("user :")
    if message:
        messages.append(
            {"role": "user",
                "content":message},
        )
        chat=openai.ChatComplition.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply= chat.choices[0].message.content
        print(f"ChatGPT:{reply}")
        messages.append({"role": "assistant", "content":reply})

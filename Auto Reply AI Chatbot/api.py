from groq import Groq
import pyperclip

client = Groq(
    api_key="Your api key"
)

# Clipboard se chat lo
command = pyperclip.paste()

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a person named Jarvis. "
                "You speak Hinglish as well as English. "
                "You analyze chat history and respond naturally like a human. "
                "Reply only to the latest message unless context is required."
                "And if want you can use emojis too to make chats more effective , also dont use too many emojis only when there is most required"
            )
        },
        {
            "role": "user",
            "content": command
        }
    ],
    temperature=0.7,
    max_tokens=300
)

print(completion.choices[0].message.content)
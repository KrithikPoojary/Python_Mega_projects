import pyautogui
from groq import Groq
import pyperclip
import time

client = Groq(
    api_key="API_KEY"
)

# 1. Chat icon pe click
pyautogui.click(1132, 872)
time.sleep(1)

# 2. Text select kar
pyautogui.moveTo(574, 214, duration=0.2)
pyautogui.mouseDown()
pyautogui.moveTo(1559, 775, duration=1)
pyautogui.mouseUp()

time.sleep(0.3)

# 3. Copy
pyautogui.hotkey("ctrl", "c")
pyautogui.click(575, 217)

time.sleep(0.3)

# 4. Clipboard se text lo
chat_text = pyperclip.paste()

print("===== CHAT =====")
print(chat_text)

command = pyperclip.paste()

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a person named K. "
                "You speak Hinglish as well as English. "
                "You analyze chat history and respond naturally like a human. "
                "Reply only to the latest message by the receiver ."
                "If there is no message by the reciver ignore the text"
                "And if want you can use emojis too to make chats more effective, also dont use too many emojis only when there is most required"
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

response = completion.choices[0].message.content
print(response)

# Chat input box pe click
pyautogui.click(668, 814)
time.sleep(0.3)

# Type/Paste response
pyperclip.copy(response)
pyautogui.hotkey("ctrl", "v")

time.sleep(0.2)

# Send
pyautogui.press("enter")
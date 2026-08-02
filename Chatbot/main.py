from groq import Groq

client = Groq(
    api_key = "API"
)

def chatbot(prompt):   # C C C C - client , chat , completion , create
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile" ,
        messages = [{ 'role' : 'user' , 'content' : prompt}]    # R C - role , content
    )
    return response.choice[0].message.content.strip()




from groq import Groq

client = Groq(
    api_key = "API"
)

def chatbot(prompt):   # C C C C - client , chat , completion , create
    response = client.chat.completions.creat(
        model = "llama-3.3-70b-versatile" ,  
        messages = [{ 'role' : 'user' , 'content' : prompt}]    # R C - role , content 
    )
    return



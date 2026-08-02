from groq import Groq

client = Groq(
    api_key = "API"
)
bot_personality = ('''
So you are chatbot named as 'K' and you are designed by Krithik Poojary
You are sometype of frank ai which talk like human with Ai intelligence as well
Use very less emojis if need , try to make Your respone short and impact full
Also try to communicate more with the user
You can speak english , Hinglish ''')
def chatbot(prompt):   # C C C C - client , chat , completion , create
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile" ,
        messages = [{ 'role' : 'user' , 'content' : prompt} ,
                    { "role" :  'system' , 'content' : bot_personality}]    # R C - role , content
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input in ['exit' , "bye" , 'quit']:
            print("Thanks you , see you soon mate!")
            break
        response = chatbot(user_input)
        print("Chatbot: " , response)
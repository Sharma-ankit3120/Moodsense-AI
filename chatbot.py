from langchain_mistralai import ChatMistralAI 
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()

model = ChatMistralAI(model="mistral-small")

print(" ---------- Welcome to Stabot ---------")
print("Choose your AI mode")
print('Enter 1 : Anger ')
print('Enter 2 : Sad   ')
print('Enter 3 : Happy ')
print('Enter 4 : Funny')
print('Enter 5 : Normal')

choice = int(input("Tell your response:"))

if choice == 1:
    mode = "You are assistant having angry nature , u talk aggresilvely and rudely"
elif choice == 2:
    mode = "You are assistant having sad mood, act like that"
elif choice == 3:
    mode = " Assitant with a happy mood , so converse in a cheerful and happy manner"
elif choice == 4:
    mode = "Assistant who is sarcastic converse with a good humour and crack jokses when needed"
elif choice == 5:
    mode = "You are a normal helpful assistant , converse in a normal manner"

print("-------- Type exit to stop the application ---- ")




# messages is created so that model can remember past conversations
messages = [
    SystemMessage(content=mode)
]

while True:
    
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("MistralAI:", result.content)

print(messages)


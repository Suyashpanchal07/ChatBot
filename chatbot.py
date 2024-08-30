def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "name" in user_input:
        return "I'm a simple rule-based chatbot."
    elif "weather" in user_input:
        return "I can't check the weather, but I hope it's nice where you are!"
    elif "time" in user_input:
        return "I can't tell the time, but I hope you're having a good day!"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "help" in user_input:
        return "I'm here to assist you. What do you need help with?"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Example interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
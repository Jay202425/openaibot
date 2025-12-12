import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_bot(user_message: str) -> str:
    """
    Send a message to the OpenAI bot and get a response.
    
    Args:
        user_message: The message to send to the bot
        
    Returns:
        The bot's response
    """
    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    return response.choices[0].message.content

def main():
    """Main function to run the bot in interactive mode."""
    print("OpenAI Bot - Type 'exit' to quit")
    print("-" * 40)
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = chat_with_bot(user_input)
            print(f"Bot: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()

import os

import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def send_to_llm(question: str) -> str:
    """Send a question to the OpenAI Responses API and return the response."""
    try:
        response = client.responses.create(
            model="gpt-3.5-turbo",
            instructions="You are a helpful assistant.",
            input=question,
        )
        return response.output_text.strip()
    except openai.APIConnectionError:
        return "Error: Failed to connect to the OpenAI API. Check your network."
    except openai.AuthenticationError:
        return "Error: Invalid API key. Please check your OPENAI_API_KEY."
    except openai.RateLimitError:
        return "Error: You’ve hit your usage or rate limit. Please check your billing and quota on the OpenAI dashboard."
    except Exception as e:
        return f"Error: An unexpected issue occurred: {str(e)}"


def handle_user_interaction() -> None:
    """Handle user input and output, looping until the user types 'exit'."""
    print("Welcome to the LLM Chatbot! Ask a question or type 'exit' to quit.")

    while True:
        user_input = input("\nYour question: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye! Hope to see you soon!")
            break

        if not user_input:
            print("Please enter a valid question.")
            continue

        response = send_to_llm(user_input)
        print("\nResponse:", response)


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found. Please set it in the .env file.")
    else:
        handle_user_interaction()

""" Main assistant module using the hyperbolic api. """
import os
from typing import Optional
from openai import OpenAI

SYSTEM_PROMPT = "You are a helpful assistant. Be helpful, kind and brief. Avoid being overly verbose!"

def get_response(client: OpenAI, messages: list) -> Optional[str]:
    """
    Create a chat completion using the given list of messages and get the model's response.

    :param client: The OpenAI client used to communicate with the inference provider.
    :param messages: The list of messages in the conversation so far.

    :return: The model's response.
    """
    chat_completion = client.chat.completions.create( # pyright: ignore [reportAttributeAccessIssue]
            model="meta-llama/Meta-Llama-3.1-405B-Instruct",
            messages=messages,
            max_tokens=1024,
            temperature=0.7
            )
    return chat_completion.choices[0].message.content

def main() -> None:
    """ The module's entrypoint. """
    client = OpenAI(
            api_key=os.environ["HYPERBOLIC_API_KEY"],
            base_url="https://api.hyperbolic.xyz/v1"
            )
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("Chat interface started. Type 'exit' to quit, 'clear' to clear conversation history.\n")
    while True:
        user_input = input("Your message: \n")
        if user_input.lower() == "exit":
            break
        if user_input.lower() == "clear":
            print("Clearing conversation history and starting new conversation.")
            messages.clear()
            messages.append({"role": "system", "content": SYSTEM_PROMPT})
            continue

        messages.append({"role": "user", "content": user_input})
        response = get_response(client, messages)
        if response:
            print(f"Assistant: \n{response}")
            messages.append({"role": "assistant", "content": response})
        else:
            print("Empty response from model, terminating!")
            break


if __name__ == "__main__":
    main()

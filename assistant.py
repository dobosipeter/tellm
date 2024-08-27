""" Main assistant module. """
import os
from fireworks.client import Fireworks


def main() -> None:
    """ The module's entry point. """
    client = Fireworks(api_key=os.environ["FIREWORKS_API_KEY"])
    conversation = []

    def send_message(message: str) -> str:
        """
        Send a message to the model.

        :param message: The message to send to the model.

        :return: The response from the model.
        """
        conversation.append({"role": "user", "content": message})

        try:
            response = client.chat.completions.create(
                model="accounts/fireworks/models/llama-v3p1-405b-instruct",
                messages=conversation,
                max_tokens=1024,
                temperature=0.7,
                top_p=1,
                stream=False
            )

            reply = response.choices[0].message.content
            conversation.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"Error: {str(e)}"

    print("Chat interface started. Type 'exit' to quit.")
    while True:
        print("\n")
        user_input = input("You: \n")
        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'clear':
            print("Clearing conversation history and starting a new conversation.\n")
            conversation.clear()
            continue
        response = send_message(user_input)
        print("\n")
        print(f"Assistant: \n{response}")

    print("Chat ended.")


if __name__ == '__main__':
    main()


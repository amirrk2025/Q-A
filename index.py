import openai


API_KEY = "YOUR_API_KEY"
openai.api_key = API_KEY
openai.api_base = "URL"


messages_list = [
    {"role": "system", "content": "You are a helpful assistant who generates questions and answers from a given text."}
]

while True:

    user_input = input("Enter the text to analyze (or type 'exit' to quit): ")


    if user_input.lower() == 'exit':
        print("Exiting... Goodbye!")
        break


    messages_list.append(
        {"role": "user", "content": f"Read the following text and generate questions with their answers:\n\n{user_input}"}
    )


    print("Connecting to the LLM...")

    try:

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages_list
        )


        assistant_message = response['choices'][0]['message']['content']

        messages_list.append(
            {"role": "assistant", "content": assistant_message}
        )

        print(f"Questions and Answers:\n{assistant_message}")

    except Exception as e:
        print(f"Error: {e}")

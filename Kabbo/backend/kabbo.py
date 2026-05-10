import ollama

print("Kabbo AI Started...")
print("Type 'exit' to stop.")

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Kabbo stopped.")
        break

    try:
        response = ollama.chat(
            model='mistral',
            messages=[
                {
                    'role': 'user',
                    'content': user
                }
            ]
        )

        print("\nKabbo:", response['message']['content'])

    except Exception as e:
        print("\nError:", e)
        print("Make sure Ollama is installed and the model is downloaded.")
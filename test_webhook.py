
import requests

url = "http://localhost:5678/webhook/6cfd066b-f593-4f2d-9c0e-b5f26f5f159b"

while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Goodbye Buddy!")
        break

    user_message = message
    request_message = {"message": user_message}

    response = requests.post(url, json=request_message)

    result = response.json()
    print("AI:" , result[0]["output"])
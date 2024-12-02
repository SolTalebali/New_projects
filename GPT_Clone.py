import os
import requests

api_key = os.getenv("MIMO_OPENAI_API_KEY")
url = "https://ai.mimo.org/v1/openai/message"
headers = {"api-key": api_key}

def send_message (user_message, thread_id):
  body = {"message": user_message}
  if thread_id:
    body["threadId"] = thread_id

  response = requests.post(url, headers=headers, json=body)
  return response.json()

current_thread_id = None

print("Welcome! Type your message and press Enter to send.")
print("Type 'new' to switch conversation thread.")
print("Type 'exit' to end the program")

while True:
  user_message = input("You: ")
  if user_message == "exit":
    break
  elif user_message == "new":
    current_thread_id = None
    print("Starting a new thread for you.\n")
    continue

  response_data = send_message(user_message, current_thread_id)
  latest_message = response_data.get("response")
  current_thread_id = response_data.get("threadId")

  print(f"GPT: {latest_message}")

threads = []
if current_thread_id not in threads:
  threads.append(current_thread_id)

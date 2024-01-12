import requests
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()

    # Only respond to messages sent by you.
    if message['sender_id'] != os.getenv('MY_SENDER_ID'):
        return

    # Respond to "hello bot".
    if "hello bot" in text:
        send_message("sup")

    # Respond to "good morning" and "good night" messages.
    if 'good morning' in text:
        send_message(f"Good morning, {message['name']}!")
    elif 'good night' in text:
        send_message(f"Good night, {message['name']}!")

    # Respond to "tell me a joke".
    if 'tell me a joke' in text:
        joke_response = requests.get('https://official-joke-api.appspot.com/jokes/random')
        joke = joke_response.json()['setup'] + " " + joke_response.json()['punchline']
        send_message(joke)

    LAST_MESSAGE_ID = message["id"]

def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()

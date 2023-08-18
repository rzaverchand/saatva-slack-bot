import requests
import time
import os

TOKEN = os.environ.get("SLACK_BOT_TOKEN")
CHANNEL_ID = None

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.get("https://slack.com/api/conversations.list", headers=headers)
channels = response.json()['channels']

for channel in channels:
    if channel['name'] == 'general':
        CHANNEL_ID = channel['id']

channel_response = requests.get(f"https://slack.com/api/conversations.history?channel={CHANNEL_ID}", headers=headers)
messages = channel_response.json()['messages']

# Delete each message
for message in messages:
    ts = message['ts']
    response = requests.post("https://slack.com/api/chat.delete", headers=headers, data={
        "channel": CHANNEL_ID,
        "ts": ts
    })
    print(f"Deleted message with timestamp {ts}")
    time.sleep(1)

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from qa_chain import get_chain

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

chatgpt_chain = get_chain("./data/saatva_data.csv")

@app.message("")
def message_handler(message, say, logger):
    response = chatgpt_chain({"question": message['text']})
    say(response['result'])

# Starts app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()



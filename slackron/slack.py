import json
import requests


class Slack:
    def __init__(self, webhook_url, channel, username, emoji):
        self._webhook_url = webhook_url
        self._channel = channel
        self._username = username
        self._emoji = emoji

    def send(self, text):
        headers = {'content-type':'application/json'}
        payload = json.dumps({
                'channel' : self._channel,
                'username' : self._username,
                'text' : text,
                'icon_emoji' : self._emoji, 
        })

        requests.post(self._webhook_url, headers=headers, data=payload)

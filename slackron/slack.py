import json
import requests


class Slack:
    def __init__(self, webhook_url, channel, username, emoji):
        self._webhook_url = webhook_url
        self._channel = channel
        self._username = username
        self._emoji = emoji
        self._status_props = {
            "failure": {
                "color": "#cb2431", "mark": ":x:", "msg": "Failure"
            },
            "success": {
                "color": "#2cbe4e", "mark": ":white_check_mark:", "msg": "Success"
            },
        }

    def generate_fields(
        self, command, status, start_date, end_date,
        stdout=None, stderr=None
    ):
        fields = [
            {"short": True, "title": "Command", "value": command},
            {"short": True, "title": "Status", "value": status},
            {"short": True, "title": "Started at", "value": start_date},
            {"short": True, "title": "Ended at", "value": end_date},
        ]
        # The following block is voluntarly commented.
        # We might want to display stdout in the future.
        # if stdout and len(stdout):
        #     fields.append(
        #         {"short": False, "title": "Console output", "value": stdout.decode()},
        #     )
        if stderr and len(stderr):
            fields.append(
                {"short": False, "title": "Error output", "value": stderr.decode()},
            )
        return fields

    def build_attachment(
        self, command, status, start_date, end_date,
        stdout=None, stderr=None
    ):
        return {
            "color": self._status_props[status]["color"],
            "title": "{mark} Task {status}".format(
                mark=self._status_props[status]["mark"],
                status=self._status_props[status]["msg"]
            ),
            "fields": self.generate_fields(
                command=command,
                status=self._status_props[status]["msg"],
                start_date=start_date,
                end_date=end_date,
                stdout=stdout,
                stderr=stderr
            )
        }

    def send(
        self, command, status, start_date, end_date,
        stdout=None, stderr=None
    ):
        headers = {'content-type':'application/json'}
        payload = json.dumps({
                "channel" : self._channel,
                "username" : self._username,
                "text" : "",
                "icon_emoji" : self._emoji,
                "attachments": [self.build_attachment(
                    command=command,
                    status=status,
                    start_date=start_date,
                    end_date=end_date,
                    stdout=stdout,
                    stderr=stderr
                )]
        })

        requests.post(self._webhook_url, headers=headers, data=payload)

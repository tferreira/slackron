from pathlib import Path
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    def __init__(self):
        self._config = load(
            open('{}/.slackron.yml'.format(str(Path.home())), 'r'),
            Loader=Loader
        )

    @property
    def webhook_url(self):
        if 'webhook_url' not in self._config:
            raise Exception('url missing in ~/.slackron.yml config file')
        return self._config['webhook_url']

    @property
    def channel(self):
        if 'channel' not in self._config:
            raise Exception('channel missing in ~/.slackron.yml config file')
        return self._config['channel']

    @property
    def username(self):
        # if not specified, it will be "Slackron"
        return self._config['username'] if 'username' in self._config else "Slackron"

    @property
    def emoji(self):
        # if not specified, it will be slack default
        return self._config['emoji'] if 'emoji' in self._config else None

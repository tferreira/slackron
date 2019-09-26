import sys
import shlex

from slackron.config import Config
from slackron.runner import Runner
from slackron.slack import Slack


def run():
    args = sys.argv[1:]
    delimiter = "--"

    if len(args) < 2:
        print("Missing command (Usage: slackron -- CMD)")
    elif args[0] != delimiter:
        print("Bad delimiter. (Usage: slackron -- CMD)")
    else:
        cmd_line_args = list(map(shlex.quote, args[1:]))

        # load config file from home directory
        config = Config()

        slack_client = Slack(
            webhook_url=config.webhook_url,
            channel=config.channel,
            username=config.username,
            emoji=config.emoji
        )

        runner = Runner(
            cmd_line_args=cmd_line_args,
            slack_client=slack_client
        )
        runner.execute()

import time
import subprocess

from datetime import datetime


class Runner():
    def __init__(self, cmd_line, slack_client):
        self._cmd_line = cmd_line
        self._slack = slack_client

    def execute(self):
        results = self.run_command()

        start_date = datetime.utcfromtimestamp(
            int(results['start_ts'])
        ).strftime('%Y-%m-%d %H:%M:%S')
        end_date = datetime.utcfromtimestamp(
            int(results['end_ts'])
        ).strftime('%Y-%m-%d %H:%M:%S')

        self._slack.send(
            command=self._cmd_line,
            status='success' if results['code'] == 0 else 'failure',
            start_date=start_date,
            end_date=end_date,
            stdout=results['stdout'],
            stderr=results['stderr']
        )

    def run_command(self):
        start_ts = time.time()

        process = subprocess.run(
            args=self._cmd_line,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

        end_ts = time.time()

        results = {
            "start_ts": start_ts,
            "end_ts": end_ts,
            "code": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr
        }

        return results

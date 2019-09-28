import time
import subprocess

from datetime import datetime


class Runner():
    def __init__(self, cmd_line_args, slack_client):
        self._cmd_line_args = cmd_line_args
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
            command=self._cmd_line_args,
            status='success' if results['code'] == 0 else 'failure',
            start_date=start_date,
            end_date=end_date,
            stdout=results['stdout'],
            stderr=results['stderr']
        )

    def run_command(self):
        start_ts = time.time()

        process = subprocess.Popen(
            args=self._cmd_line_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        end_ts = time.time()

        results = {
            "start_ts": start_ts,
            "end_ts": end_ts,
            "code": process.returncode,
            "stdout": stdout,
            "stderr": stderr
        }

        return results

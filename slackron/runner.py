import time
import subprocess

from datetime import datetime


class Runner():
    def __init__(self, cmd_line, slack_client):
        self._cmd_line = cmd_line
        self._slack = slack_client

    def execute(self):
        results = self.run_command()

        report = self.build_report(
            start_ts=int(results['start_ts']),
            end_ts=int(results['end_ts']),
            status="OK" if results['code'] == 0 else "FAILED",
            stdout=results['stdout'].decode(),
            stderr=results['stderr'].decode()
        )

        self._slack.send("\n".join(report))

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

    def build_report(self, start_ts, end_ts, status,
                    stdout=None, stderr=None):
        report = [
            "**Cron report**",
            "_Command_: {}".format(self._cmd_line),
            "_Started_: {}".format(
                datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d %H:%M:%S')
            ),
            "_Ended_: {}".format(
                datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d %H:%M:%S')
            ),
            "_Status_: {}".format(status),
        ]

        if stderr and stderr != "":
            report.append("_Reason_: {}".format(stderr))

        return report
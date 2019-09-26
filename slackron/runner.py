import time
import subprocess

from datetime import datetime


class Runner():
    def __init__(self, cmd_line_args, slack_client):
        self._cmd_line_args = cmd_line_args
        self._slack = slack_client

    def execute(self):
        results = self.run_command()

        report = self.build_report(
            start_ts=int(results['start_ts']),
            end_ts=int(results['end_ts']),
            status="OK" if results['code'] == 0 else "FAILED",
            stdout=results['stdout'],
            stderr=results['stderr']
        )

        self._slack.send("\n".join(report))

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

    def build_report(self, start_ts, end_ts, status,
                    stdout=None, stderr=None):
        report = [
            "**Cron report**",
            "_Command_: {}".format(self._cmd_line_args),
            "_Started_: {}".format(
                datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d %H:%M:%S')
            ),
            "_Ended_: {}".format(
                datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d %H:%M:%S')
            ),
            "_Status_: {}".format(status),
        ]

        if stderr and stderr != "":
            report.append("_Reason_: {}".format(stderr.decode()))

        return report
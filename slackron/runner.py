import subprocess


class Runner():
    def __init__(self, cmd_line, slack_client):
        self._cmd_line = cmd_line
        self._slack = slack_client

    def execute(self):
        result = self.run_command()
        self._slack.send(result)

    def run_command(self):
        process = subprocess.run(
            args=self._cmd_line,
            shell=True,
            capture_output=True
        )

        if process.returncode == 0:
            # success
            result = process.stdout
        else:
            # failure
            result = process.stderr

        return result.decode()

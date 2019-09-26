# slackron

**slackron** is a Python wrapper to notify about cronjob execution to **Slack**.

## Installation

slackron is available on [pypi.org](https://pypi.org/project/slackron/).

## Configuration

slackron will look for the following configuration file on your home directory: `~/.slackron.yml`

Example:
```yaml
    webhook_url: https://hooks.slack.com/services/T00/B00/XXXXXXXXXXXX
    channel: "#cron"
    username: Slackron
    emoji: robot
```

## Usage

```sh
*/1 * * * * slackron -- wget -Ss https://example.com
```

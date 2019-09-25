# slackron

**slackron** is a Python wrapper to notify about cronjob execution to **Slack**.

## Installation

slackron is available on [pypi.org](https://pypi.org/project/slackron/).

## Configuration

slackron will look for the following configuration file on your home directory: `~/.slackron`

## Usage

```sh
*/1 * * * * slackron -- wget -Ss https://example.com
```

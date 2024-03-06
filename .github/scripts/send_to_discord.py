from github import Github
import requests
import os
import datetime
import re


def send_discord_message(webhook_url, message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()


def split_message(content):
    SEPARATOR = '\u200B\n'

    sections = []
    current_section = []

    for line in content.split('\n'):
        if line.startswith('#') and current_section:
            sections.append(SEPARATOR.join(current_section))
            current_section = []
        current_section.append(line)
    
    if current_section:
        sections.append(SEPARATOR.join(current_section))
    
    return sections


GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
DISCORD_MAX_MESSAGE_LENGTH = 2000

g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPOSITORY)

today = datetime.date.today()
formatted_date = today.strftime('%Y/%m/%d')
file_path = f"src/{formatted_date}/meeting.md"

try:
    contents = repo.get_contents(file_path, ref="main")
    file_content = contents.decoded_content.decode('utf-8')
    messages = split_message(file_content)

    for message in messages:
        send_discord_message(DISCORD_WEBHOOK_URL, message)
        print("Part of the message sent to Discord successfully.")

except Exception as e:
    print(f"Failed to send message to Discord or file not found: {e}")

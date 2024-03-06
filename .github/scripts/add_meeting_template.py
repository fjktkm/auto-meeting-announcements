from github import Github
import datetime
import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')

g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPOSITORY)

next_week = datetime.date.today() + datetime.timedelta(days=7)
formatted_date = next_week.strftime('%Y/%m/%d')
file_path = f"src/{formatted_date}/meeting.md"

template_path = 'templates/meeting.md'
with open(template_path, 'r') as file:
    template_content = file.read()

try:
    repo.get_contents(file_path, ref="main")
    print(f"File already exists at {file_path}, no action taken.")
except:
    repo.create_file(file_path, "auto: 部会用のテンプレートを追加", template_content, branch="main")
    print(f"File created at {file_path}.")

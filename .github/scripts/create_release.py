from github import Github
import datetime
import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')

g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPOSITORY)

today = datetime.datetime.now()

formatted_date = today.strftime('%Y/%m/%d')
file_path = f"src/{formatted_date}/meeting.md"

formatted_datetime = today.strftime('%Y-%m-%d-%H-%M')
tag_name = f"meeting-{formatted_datetime}"
release_name = f"部会 {formatted_datetime}"

try:
    with open(file_path, 'r') as file:
        meeting_notes = file.read()
    
    release = repo.create_git_release(tag=tag_name, name=release_name, message=meeting_notes, draft=False, prerelease=False)
    print(f"Release created: {release.html_url}")
except FileNotFoundError:
    print(f"File {file_path} not found.")

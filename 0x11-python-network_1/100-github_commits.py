#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of a GitHub repository"""


import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors

        commits = response.json()

        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

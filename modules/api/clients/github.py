import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def get_commits(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        body = r.json()

        return body

    def get_code_of_conduct(self, key):
        r = requests.get(f"https://api.github.com/codes_of_conduct/{key}")
        body = r.json()

        return body

    def get_code_of_conduct_status(self, key):
        r = requests.get(f"https://api.github.com/codes_of_conduct/{key}")
        status = r.status_code

        return status

import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name})
        body = r.json()

        return body
    
    def user_follows_target_user (self, username, target_user):
        r = requests.get(f"https://api.github.com/users/{username}/following/{target_user}")
        code = r.status_code

        return code

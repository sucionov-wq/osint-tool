import requests

def check_username(username):
    url = f"https://github.com/{username}"
    r = requests.get(url)

    return {
        "username": username,
        "github_exists": r.status_code == 200
    }

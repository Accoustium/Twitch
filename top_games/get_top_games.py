import os
import requests


def main():
    response = requests.get(
        "https://api.twitch.tv/helix/games/top",
        headers={
            "Authorization": f"Bearer {os.environ.get('ACCESS_TOKEN')}",
            "Client-Id": os.environ.get("CLIENT_ID")
        }
    )
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

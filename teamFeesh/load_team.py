import os
import requests

def main():
    response = requests.get(
        f"https://api.twitch.tv/helix/teams?name={os.environ.get('TWITCH_TEAM')}",
        headers={
            "Authorization": f"Bearer {os.environ.get('ACCESS_TOKEN')}",
            "Client-Id": os.environ.get("CLIENT_ID")
        }
    )

    print(response.content)
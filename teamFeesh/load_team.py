import os
import requests

def main():
    response = requests.get(
        "https://api.twitch.tv/helix/teams?name=feeshtank",
        headers={
            "Authorization": f"Bearer {os.environ.get('ACCESS_TOKEN')}",
            "Client-Id": os.environ.get("CLIENT_ID")
        }
    )

    print(response.content)
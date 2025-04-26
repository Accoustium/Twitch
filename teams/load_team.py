import os
import requests

CURR_DIR = os.getcwd()

def main(team):
    response = requests.get(
        f"https://api.twitch.tv/helix/teams?name={team}",
        headers={
            "Authorization": f"Bearer {os.environ.get('ACCESS_TOKEN')}",
            "Client-Id": os.environ.get("CLIENT_ID")
        }
    )

    print(str(response.content))

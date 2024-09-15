import os
import requests
import bs4


def main():
    url = "https://www.twitch.tv/drops/campaigns"
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {os.environ.get('ACCESS_TOKEN')}",
            "Client-Id": os.environ.get("CLIENT_ID")
        }
    )

    if response.status_code == 200:
        read_content(response.content)

    print(response.status_code)
    print(response.content)


def read_content(html_content):
    print(html_content)
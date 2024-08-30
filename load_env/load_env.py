import os
import dotenv
import requests
from textwrap import dedent
from twitch_auth import auth


def main():
    print("Loading Environment Variables")
    if dotenv.load_dotenv("./load_env/.env"):
        try:
            if os.environ.get('ACCESS_TOKEN') is None:
                raise KeyError()
            print("Access Token Found")
            validate()
        except KeyError:
            print("Access Token NOT Found")
            get_auth()
    else:
        print("Failed to Load Environment Variables")


def validate():
    url = "https://id.twitch.tv/oauth2/userinfo"
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {os.environ.get('ACCESS_TOKEN')}",
            "Client-Id": os.environ.get("CLIENT_ID")
        }
    )

    if response.status_code == 200:
        print("Token Validated")


def get_auth():
    variables = auth.main()
    save_env(variables)

def save_env(url_vars: dict):
    if "access_token" in url_vars.keys() and "id_token" in url_vars.keys():
        with open('./load_env/.env', 'w') as f:
            f.write(
                dedent(
                    f"""# Channel setting for Bot
                    CHANNEL={os.environ.get('CHANNEL')}
                    NICK={os.environ.get('NICK')}
                    CLIENT_ID={os.environ.get('CLIENT_ID')}
                    ACCESS_TOKEN={url_vars["access_token"]}
                    ID_TOKEN={url_vars["id_token"]}
                    """
                )
            )

    main()

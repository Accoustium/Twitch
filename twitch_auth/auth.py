import os
import requests
import webbrowser
import dotenv


# Load Environment Variables
dotenv.load_dotenv("./twitch_auth/.env")
# Setting up URL for Twitch
AUTH_URL = "https://id.twitch.tv/oauth2/authorize"
CSRF_TOKEN = "c3ab8aa609ea11e793ae92361f002671"
URL = AUTH_URL + "?response_type=token+id_token" \
    + f"&client_id={os.environ.get('CLIENT_ID')}" \
    + f"&redirect_uri={os.environ.get('REDIRECT_URI')}" \
    + "&scope=analytics%3Aread%3Aextensions+analytics%3Aread%3Agames+openid" \
    + f"&state={CSRF_TOKEN}"
# Setting up Chrome Client
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(CHROME_PATH))


def main():
    response = requests.get(URL)
    if response.status_code == 200:
        webbrowser.get('chrome').open(URL, new=2) # This Opens a new Chrome tab

    redirect = input("Enter URL Redirect from Twitch: ")
    variables = dict()
    for var in redirect.split("#")[1].split("&"):
        k, v = var.split("=")
        variables.update({k: v})

    return variables

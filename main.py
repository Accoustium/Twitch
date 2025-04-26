import os

from load_env import load_env
from teams import load_team
from top_games import get_top_games
from drop_campaigns import get_campaigns


if __name__ == "__main__":
    load_env.main()
    for team in os.environ.get("TWITCH_TEAM").split(","):
        load_team.main(team)
    # get_top_games.main()
    # get_campaigns.main()
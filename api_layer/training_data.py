from api_layer import gamepedia_api as gapi
from api_layer import riot_api


def load_train_data():
    return 0


def load_challenger_data():
    challenger = riot_api.get_challengers()
    return challenger


def load_current_lcs_players():
    lcs_players = gapi.get_current_lcs()
    return lcs_players

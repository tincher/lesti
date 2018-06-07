from api_layer import riot_api


def load_challenger_data():
    challenger = riot_api.get_challengers()
    return challenger


def load_current_lcs_players():
    riot_api.get_current_lcs()

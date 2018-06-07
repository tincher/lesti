from api_layer import gamepedia_api
from api_layer import riot_api


def load_train_data():
    train_x = []
    train_y = []
    return


def load_train_data_only_player(name):
    match_ids = riot_api.get_match_ids(name)
    return list(map(lambda m_id: riot_api.get_match(m_id), match_ids))


def load_train_data_whole_game():
    return


def load_challenger_data():
    challenger = riot_api.get_challengers()
    return challenger


def load_current_lcs_players():
    lcs_players = gamepedia_api.get_current_lcs()
    return lcs_players

# tmp = load_train_data_only_player('bigmcjoe')
# with open('data.json', 'w') as outfile:
#     json.dump(tmp, outfile)
# print(tmp)

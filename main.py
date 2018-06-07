import time
from api_layer import training_data as td
from api_layer import riot_api


def main():
    challengers = td.load_challenger_data()
    print(riot_api.get_account('EPiC majo'))


main()

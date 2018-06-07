from api_layer import riot_api as rapi
from api_layer import training_data as td


def main():
    challengers = td.load_challenger_data()
    print(rapi.get_account('EPiC majo'))


main()

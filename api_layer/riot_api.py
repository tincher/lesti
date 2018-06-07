import requests
from string import Template

headers = {'X-Riot-Token': 'RGAPI-2780f9b8-94d3-4d51-9f4d-c406fe5f25e7'}

ranked_extension = '?queue=4&queue=6&queue=42&queue=410&queue=420&queue=440'
base_url = 'https://euw1.api.riotgames.com/lol/'

raw_url_summoner_id = Template(base_url + 'summoner/v3/summoners/by-name/$name')
raw_url_match_list = Template(base_url + 'match/v3/matchlists/by-account/$id')

challenger_url = base_url + 'league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5'


def get_challengers():
    return requests.get(challenger_url, headers=headers).json()


def get_account(name):
    return requests.get(raw_url_summoner_id.substitute(name=name), headers=headers).json()


def get_match_list(account_id):
    return requests.get(raw_url_match_list.substitute(id=account_id), headers=headers).json()


def get_ranked_matches(name):
    account_id = get_account(name).get('accountId')
    return requests.get(raw_url_match_list.substitute(id=account_id) + ranked_extension, headers=headers).json()

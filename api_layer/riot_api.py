import time
from time import sleep

import requests

from api_layer import url_builder

headers = {'X-Riot-Token': 'RGAPI-9db58bc2-97b2-42f9-a9cc-f28569151042'}


def get_match(match_id):
    return get_request(url_builder.match(match_id))


def get_match_ids(name):
    return list(map(lambda x: x['gameId'], get_matches_from_last_months(name, 6)))


def get_matches_from_last_months(name, months):
    start_time = int((time.time() - (60 * 60 * 24 * 30 * months)) * 1000)
    account_id = get_account_id(name)
    return get_match_list_from_last_months(account_id, start_time)


def get_match_list_from_last_months(account_id, start_time):
    end, begin_index = -1, 0
    result = []
    while begin_index > end:
        r = get_request(url_builder.match_list(account_id, start_time, begin_index))
        end = r['totalGames']
        begin_index = r['endIndex']
        result += r['matches']
    return result


def get_challengers():
    return get_request(url_builder.get_challenger_url())


def get_account_id(name):
    return get_request(url_builder.account_url(name))['accountId']


def get_request(url):
    status_code = 0
    i = 0
    while status_code != 200:
        r = requests.get(url, headers=headers)
        status_code = r.status_code
        if r.reason == 'Too Many Requests':
            i += 1
            print('sleeping due to too many requests for ' + (120 - 110 / i))
            sleep(120 - 110 / i)
    return r.json()

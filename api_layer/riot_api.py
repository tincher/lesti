import time

import requests

from api_layer import url_builder

headers = {'X-Riot-Token': 'RGAPI-9db58bc2-97b2-42f9-a9cc-f28569151042'}


def matches_from_last_months(name, months):
    start_time = int((time.time() - (60 * 60 * 24 * 30 * months)) * 1000)
    print(start_time)
    account_id = get_account(name)['accountId']
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
    return get_request(url_builder.challenger_url())


def get_account(name):
    return get_request(url_builder.account_url(name))


def get_request(url):
    return requests.get(url, headers=headers).json()


# matches_from_last_months('a', 6)
# print(get_account('bigmcjoe'))
print(matches_from_last_months('bigmcjoe', 6))

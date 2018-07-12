from string import Template

base_url = 'https://euw1.api.riotgames.com/lol/'

raw_url_summoner_id = Template(base_url + 'summoner/v3/summoners/by-name/$name?')
raw_url_match_list = Template(base_url + 'match/v3/matchlists/by-account/$id?')
raw_url_match = Template(base_url + 'match/v3/matches/$id?')

challenger_url = base_url + 'league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5'

# https://euw1.api.riotgames.com/lol/match/v3/matches/3228724210
ranked_extension = 'queue=4&queue=6&queue=42&queue=410&queue=420&queue=440&'
start_time_extension = Template('beginTime=$stime&')
begin_index_extension = Template('beginIndex=$bindex&')
end_index_extension = Template('endIndex=&eindex&')


def get_challenger_url():
    return challenger_url


def match(match_id):
    return raw_url_match.substitute(id=match_id)


def match_list(account_id, start_time, begin_index):
    return raw_url_match_list.substitute(id=account_id) \
           + ranked_extension + start_time_extension.substitute(stime=start_time) \
           + begin_index_extension.substitute(bindex=begin_index)


def account_url(name):
    return raw_url_summoner_id.substitute(name=name)

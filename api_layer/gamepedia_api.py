import requests
from bs4 import BeautifulSoup

gp_base_url = 'https://lol.gamepedia.com/'
gp_current_players = gp_base_url + 'LCS_Players/Current'


def get_current_lcs():
    content = requests.get(gp_current_players).text
    soup = BeautifulSoup(content, 'html.parser')
    ls = soup.find_all('td', class_='field_ID')
    return list(map(lambda pro: pro.text, ls))

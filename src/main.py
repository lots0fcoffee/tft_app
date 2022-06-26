"""
MVP:
This project will show my last ten ranked games with my placement. There will be a refresh
button that I can hit whenever.

Stretch Goals:
- This app will show the comp and units played
- Not just me, enter username field
"""

import json
from numpy import average
import requests
from src import summoner_class
from src import match_class

def get_request(html: str) -> json:
    match_data = requests.get(f'{html}', 
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-492d7967-93de-4ce7-8578-df3565636867"})
    match_data = match_data.json()
    return match_data

def init_summoner(summoner: object) -> object:
    summoner.set_puuid("dlxX-iUghrcm3LBX5L5jCbXlbhKYexi06u-jxUc9u_k56ecxloI2o8SQzPfFJdHwYm3qRmJ3gGJnXQ")
    summoner.set_summoner_name("lots of coffee")
    return summoner

def request_matches(summoner: object) -> json:
    matches = get_request('https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/dlxX-iUghrcm3LBX5L5jCbXlbhKYexi06u-jxUc9u_k56ecxloI2o8SQzPfFJdHwYm3qRmJ3gGJnXQ/ids?start=0&count=50')
    return matches

def init_match_list(matches: list) -> list:
    matches_ret = []
    for match in matches:
        match_data = get_request(f'https://americas.api.riotgames.com/tft/match/v1/matches/{match}'), 
        info = match_data[0]["info"]
        if info["queue_id"] != 1100: # We only want data from ranked games
            continue
        match_obj = match_class.Match(f"{match}")
        for part in info["participants"]:
            if part["puuid"] == "dlxX-iUghrcm3LBX5L5jCbXlbhKYexi06u-jxUc9u_k56ecxloI2o8SQzPfFJdHwYm3qRmJ3gGJnXQ":
                match_obj.set_place(part["placement"])
        matches_ret.append(match_obj)
        if len(matches_ret) == 10:
            break
    return matches_ret

def main():
    summoner = summoner_class.Summoner('lots of coffee')
    summoner = init_summoner(summoner)
    
    summoner.set_matches(request_matches(summoner))
    
    matches = init_match_list(summoner.get_matches())
    
    places = []
    for m in matches:
        places.append(m.get_place())
    avg = average(places)
    print(places, avg)

if __name__ == '__main__':
    main()
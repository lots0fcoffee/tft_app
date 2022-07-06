"""
MVP:
This project will show my last ten ranked games with my placement. There will be a refresh
button that I can hit whenever.

Stretch Goals:
- This app will show the comp and units played
- Not just me, enter username field
"""

import json
from time import sleep
from numpy import average
import requests
from src import common_database, summoner_class, match_class
from src.config.config import config
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def get_request(html: str) -> json:
    api_key = config["api_key"]
    logging.info("Sending request to Riot's servers")
    try:
        riot_data = requests.get(f'{html}', 
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": f"{api_key}"})
    except requests.exceptions.RequestException as e:
        logging.error("Error: Cannot connect to Riot's servers")
    return riot_data.json()

def init_summoner(summoner: object) -> object:
    summoner.set_puuid("dlxX-iUghrcm3LBX5L5jCbXlbhKYexi06u-jxUc9u_k56ecxloI2o8SQzPfFJdHwYm3qRmJ3gGJnXQ")
    summoner.set_summoner_name("lots of coffee")
    return summoner

def request_matches(summoner: object) -> json:
    return get_request(f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{summoner.get_puuid()}/ids?start=0&count=50')

def init_match_list(matches: list, summoner: object) -> list:
    matches_ret = []
    db = common_database.Database()
    puuid = summoner.get_puuid()
    for match in matches:
        l = db.select(f"select * from dbo.Matches where match_id = '{match}' and puuid = '{puuid}'")
        norms_check = db.select(f"select * from dbo.Normal_or_Double_Up where match_id = '{match}' and puuid = '{puuid}'")
        if norms_check != []: continue
        match_obj = match_class.Match(f"{match}")
        match_obj.set_puuid(puuid)        
        if l != []:
            match_obj.set_place(l[0][2])
        else:
            match_data = get_request(f'https://americas.api.riotgames.com/tft/match/v1/matches/{match}'), 
            sleep(0.2)
            info = match_data[0]["info"]
            for part in info["participants"]:
                if part["puuid"] == puuid:
                    match_obj.set_place(part["placement"])
                    break
            place = match_obj.get_place()            
            if info["queue_id"] != 1100: # We only want data from ranked games
                db.insert(f"insert into dbo.Normal_or_Double_Up (match_id, puuid, placement) values('{match}','{puuid}',{place})")    
                continue
            db.insert(f"insert into dbo.Matches (match_id, puuid, placement) values('{match}','{puuid}',{place})")       
        matches_ret.append(match_obj)
        if len(matches_ret) == 10:
            break
    db.close_connection()
    return matches_ret

def init_summoner_and_matches() -> list:
    summoner = summoner_class.Summoner('lots of coffee')
    summoner = init_summoner(summoner)
    summoner.set_matches(init_match_list(request_matches(summoner), summoner))
    return summoner

def refresh_matches(summoner: object) -> None:
    summoner.set_matches(init_match_list(request_matches(summoner), summoner))

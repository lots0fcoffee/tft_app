from unicodedata import name


class Summoner:
    def __init__(self, summoner_name):
        self.summoner_name = summoner_name
    
    def get_summoner_name(self):
        return self.summoner_name
    
    def get_puuid(self):
        return self.puuid

    def get_matches(self):
        return self.matches
    
    def set_summoner_name(self,summoner_name):
        self.summoner_name = summoner_name

    def set_puuid(self,puuid):
        self.puuid = puuid

    def set_matches(self,matches):
        self.matches = matches
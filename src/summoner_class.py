class Summoner:
    def __init__(self, summoner_name: str) -> None:
        self.summoner_name = summoner_name
    
    def get_summoner_name(self) -> str:
        return self.summoner_name
    
    def get_puuid(self) -> str:
        return self.puuid

    def get_matches(self) -> list:
        return self.matches
    
    def set_summoner_name(self, summoner_name: str) -> None:
        self.summoner_name = summoner_name

    def set_puuid(self, puuid: str) -> None:
        self.puuid = puuid

    def set_matches(self, matches: list) -> None:
        self.matches = matches
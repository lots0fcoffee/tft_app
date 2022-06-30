class Match:
    def __init__(self, match_id: str):
        self.match_id = match_id
    
    def set_match_id(self, match_id: str) -> None:
        self.match_id = match_id
    
    def get_match_id(self) -> str:
        return self.match_id
    
    def set_place(self, place: int) -> None:
        self.place = place

    def get_place(self) -> int:
        return self.place

    def set_puuid(self, puuid: str) -> None:
        self.puuid = puuid

    def get_puuid(self) -> str:
        return self.puuid
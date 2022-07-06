from tkinter import *
from src import main
from numpy import average

class GUI:
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("600x150")
        self.root.title('TFT Placements')
        self.root.resizable(0, 0)

        self.lab = Label(self.root,font=("Arial",25))
        self.lab.pack()

        self.get_places(False)

        self.refresh_button = Button(
        self.root,
        text='Refresh',
        command=lambda: self.get_places(True))

        self.refresh_button.pack(ipadx=5, ipady = 5, expand = True)

    
    def get_places(self, refresh: bool) -> None:
        if refresh == False:
            self.summoner = main.init_summoner_and_matches()
        else:
            main.refresh_matches(self.summoner)
        
        places = []
        for m in self.summoner.get_matches():
            places.append(m.get_place())
        avg = average(places)
        p = ""
        for place in places: p += f"{place} "
        self.lab.config(text=f"Last ten placements: {p}\n Avg: {avg}")
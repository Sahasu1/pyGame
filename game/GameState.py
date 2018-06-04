import random
from locations.LocationForest import LocationForest


class GameState:

    def __init__(self, player):
        self.player = player

    gameAct = 0
    gameLocation = 0
    CurrentLocation = object

    def getLocation(self):
        return random.randint(1, 1)

    def startLocation(self):
        if self.gameLocation == 0:
            print('Вы в начеле пути')
        elif self.gameLocation == 1:
            self.CurrentLocation = LocationForest(self.player)
            print('Вы попали в лес')
            self.CurrentLocation.getEvent()
        elif self.gameLocation == 2:
            print('локациа в разработке')

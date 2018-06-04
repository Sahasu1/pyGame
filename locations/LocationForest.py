import random


class LocationForest:
    def __init__(self, player):
        self.player = player

    def slip(self):
        print('Вы отдохнули и полностью востановили здоровье')
        self.player.health = self.player.maxPlayerHealth

    def battle(self):
        pass

    def getEvent(self):
        event = random.randint(1, 2)
        if event == 1:
            print('Вы нашли стоянку')
            print('Вы можете спать - 1, приготовить поесть - 2(в  разработке)')
            player_input = int(input())
            if player_input == 1:
                self.slip()
            else:
                print('не известное действие у костра')

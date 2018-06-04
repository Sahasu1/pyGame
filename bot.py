from game.GameState import GameState


class Hero:
    maxPlayerHealth = 20
    health = 20
    agility = 1
    strength = 1
    intellect = 1

    def getStatus(self):
        print('_______')
        print('Здоровье персонажа ' + str(self.maxPlayerHealth) + '/' + str(self.health))
        print('Статы:'
              '\nЛовкость:' + str(self.agility)
              + '\nСила:' + str(self.strength)
              + '\nИнтелект:' + str(self.intellect)
              )
        print('|______|')


def gameAct(GameState):
    player_input = int(input())
    if player_input == 1:
        GameState.gameLocation = GameState.getLocation()
    elif player_input == 3:
        player.getStatus()
    else:
        print('не существует действия ' + player_input)
    GameState.startLocation()


def startGame():
    global player, GameState
    player = Hero()
    GameState = GameState(player)

    print('Прошло уже 3 дня с момента вашего путешествия.')
    # тут надо что то типо генератора предистории как получил меч и т.п.
    print('В дороге много что произошно, но вы полны решимости идти дальше...')

    while True:
        print('Выберете действие')
        print('Идти дальше - 1, Рюкзак - 2, 3 - Состояние персонажа')
        gameAct(GameState)


startGame()

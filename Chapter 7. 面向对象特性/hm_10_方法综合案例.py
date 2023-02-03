class Game(object):
    top_score = 0

    def __init__(self, name):
        self.player_name = name

    @staticmethod
    def show_help():
        print("显示帮助信息")

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def start_game(self):
        print("%s 开始游戏" % self.player_name)


Game.show_help()

Game.show_top_score()

player1 = Game("小明")
player1.start_game()

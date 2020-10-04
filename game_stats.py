class Gamestats():
    def __init__(self, ai_settings,username):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.level = 1
        self.username=username
        self.acquire_history_score()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

    def acquire_history_score(self):
        history_file="{}.txt".format(self.username)
        try:
            with open (history_file,'r')as file:
                m=file.read()
        except FileNotFoundError:
            self.history_score=0
        else:
            with open(history_file,'r')as file:
              self.history_score=int(file.read())
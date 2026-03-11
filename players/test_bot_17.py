from engine.player_interface import Bot
import random

class TestBot17(Bot):
    def __init__(self):
        super().__init__("TestBot_17")

    def get_action(self, game_state):
        return random.choice([('call', 0), ('fold', 0)])

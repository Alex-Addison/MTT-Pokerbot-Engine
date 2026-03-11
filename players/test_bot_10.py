from engine.player_interface import Bot
import random

class TestBot10(Bot):
    def __init__(self):
        super().__init__("TestBot_10")

    def get_action(self, game_state):
        return random.choice([('call', 0), ('fold', 0)])

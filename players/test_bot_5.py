from engine.player_interface import Bot
import random

class TestBot5(Bot):
    def __init__(self):
        super().__init__("TestBot_5")

    def get_action(self, game_state):
        return random.choice([('call', 0), ('fold', 0)])

import os

def generate():
    players_dir = "players"
    if not os.path.exists(players_dir):
        os.makedirs(players_dir)
        
    for i in range(1, 51):
        filename = os.path.join(players_dir, f"test_bot_{i}.py")
        content = f"""from engine.player_interface import Bot
import random

class TestBot{i}(Bot):
    def __init__(self):
        super().__init__("TestBot_{i}")

    def get_action(self, game_state):
        return random.choice([('call', 0), ('fold', 0)])
"""
        with open(filename, "w") as f:
            f.write(content)
            
    print("Generated 50 test bots.")

if __name__ == "__main__":
    generate()

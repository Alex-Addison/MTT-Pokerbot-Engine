# Python Multi-Table Tournament (MTT) Pokerbot Engine

Welcome to the **Python MTT Pokerbot Engine**! This program allows you to write your very own Artificial Intelligence "Poker Bots" using Python, and pit them against each other in massive, multi-table simulated poker tournaments. 

This engine is designed to handle all the complicated poker math (like dealing cards, moving chips, increasing blinds, and merging tables as players bust out), so you can focus entirely on writing the coolest, smartest strategies!

Have no experience running complex code? No problem! This incredibly detailed guide assumes **no prior experience** with running servers, git, or advanced python. Follow along step-by-step to run your first simulation.

---

## 🚀 Step 1: Installing the Prerequisites

To run this engine, you need **Python** to run the code. 

1. **Download Python:**
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Click the big yellow button to download Python (make sure it's at least version 3.10+).
   - **CRITICAL STEP (Windows Users):** When you run the installer you downloaded, look at the very bottom of the first screen. Make sure the checkbox that says **"Add Python to PATH"** is **CHECKED** before you click Next. This lets your computer know where python is!

2. **Open your Terminal (Command Prompt):**
   - Press the `Windows Key`, type `cmd`, and hit Enter. You should see a black text box pop up. (If on Mac, press Cmd+Space, type `Terminal`, and hit Enter).

---

## 📦 Step 2: Preparing the Engine

Now that Python is installed, we need to download the code and install its "dependencies". Dependencies are simply tools other people wrote that our project needs to function (for example, we use a tool called `treys` to evaluate which poker hand wins the pot!).

1. **Get the Code:** 
   - Since you have this file open, you already have the folder! Open your Terminal (Command line) from Step 1.
   - We need to tell the terminal to look inside this specific folder.
   - Run this command (replace the path with wherever you saved the `MTT-Pokerbot-Engine` folder):
     `cd C:\Users\Alex\Desktop\MTT-Pokerbot-Engine`
     *(Hint: You can type `cd ` with a space, then drag and drop the folder from your file explorer right into the black terminal window and hit Enter!)*

2. **Install the Libraries:**
   - In your terminal window that is now pointing to the project folder, copy and paste this command and hit Enter:
     `python -m pip install -r requirements.txt`
   - Your computer will download the `treys`, `numpy`, and `pandas` libraries. You will see some loading bars. Wait until they finish!

---

## 🤖 Step 3: Getting to Know the Bots

Inside the folder, you will see a folder called `players`. This is where all the bots live! Let's look at how to make one.

### Bot Rules
To ensure fairness, bots currently are strictly limited visually to exactly what you'd see sitting at a poker table. 

**Allowed Code Resources:** By default, bots are only allowed to use standard basic python, plus these specific libraries to help code advanced machine-learning math:
*   `math`
*   `random`
*   `numpy` (Powerful array computing for probabilities)
*   `pandas` (Powerful data analysis tools)

If a bot tries to use something like `os` to cheat or steal files, the engine will automatically block it from playing!

### How to Create a Bot
Every bot is a simple python file. You can see examples in `players/random_bot.py`.
There is only one rule: Your bot must have a `get_action` function that takes in the `game_state` and returns an action.

**The Game State dictionary gives you:**
*   `hole_cards`: Your two hidden cards
*   `board_cards`: The cards on the table
*   `pot_size`: Total chips in the pot
*   `stack_size`: Your chips remaining
*   `call_amount`: Exactly how many chips you owe to stay in the hand
*   `min_raise`: The rules on what you must bet if you want to raise
*   `blinds`: The current blind level
*   `active_players`: How many people are left in the hand

**Your Bot can return one of three things:**
1.  `return ('fold', 0)` (Give up)
2.  `return ('call', 0)` (Match the current bet to see the next card. *If call_amount is 0, this acts as checking!*)
3.  `return ('raise', 200)` (Match the bet, then add 200 more chips on top of it)

**Note:** The Engine gives bots exactly **500 milliseconds (half a second) to decide**. If your bot takes too long doing complex math, the dealer will automatically fold your hand!

### 📚 Need Help Writing a Smart Bot?
Writing a great poker bot involves understanding game theory, probability, and hand strength! Here are great places to start learning how to evaluate poker mathematically:
*   [MIT's Pokerbots Course Lectures (Free)](https://pokerbots.org/) - World class AI teaching explicitly for this!
*   [Introduction to Poker Strategy & Math](https://www.upswingpoker.com/poker-strategy/)
*   [Treys Hand Evaluator Docs](https://github.com/ihendley/treys) - Learn how your bots hole cards are formatted as numbers to do math on them.

---

## ⚙️ Step 4: Configuring the Tournament

There is a file called `config.json`. You can open this in Notepad or any text editor!

It controls everything about the simulation:
*   `simulation_count`: E.g., `100`. The engine will blast through 100 complete tournaments in parallel!
*   `starting_stack`: E.g., `1500`. Chips everybody starts with.
*   `blinds_schedule`: You can edit exactly what the blinds are.
*   `bot_decision_timeout_ms`: The 500ms limit!
*   `payouts`: Set the percentages. `"1": 0.50` means 1st place gets 50% of the prize pool!

---

## 🏃 Step 5: Start the Action!

We are ready to run a simulation!

In your terminal (the black box) pointing to the project folder:
1.  Type:
    `python main.py`
2.  Hit Enter!

The Engine will automatically load every single `.py` file inside the `players` folder and begin organizing them into 9-max tables. Because the engine is highly optimized utilizing "multiprocessing", it will run multiple entire tournaments simultaneously across your CPU cores.

**When it finishes:**
1.  It creates a cleanly organized `simulation_results.csv` file that you can open in Excel to analyze exactly which bot placed where!
2.  It creates incredibly detailed second-by-second logs inside the `/logs/` folder!

---

## 🍿 Step 6: Watch the Replay (Visualizer)

Spreadsheets are boring. What if you want to physically watch the tournament unfold, pause the action, and inspect a huge bluff? We have a built-in website for that!

1. In your terminal, type:
   `python server.py`
   and hit Enter.
2. The terminal will say `Serving at http://localhost:8000/visualizer`.
3. Open your favorite web browser (Chrome, Edge, Safari, etc).
4. In the top URL bar, copy and paste this exact link:
   `http://localhost:8000/visualizer`
5. You are in! 
   - Click the blue "Load Simulation" button at the top.
   - Go to the `logs` folder we made earlier, and select `sim_1.json`.
   - Hit the **Play ▶** button at the bottom!
   - You can increase the speed to 5x or 10x using the buttons in the corner.
   - You can see the tables coalescing dynamically. **Click on one of the round tables to zoom in** and see the actual cards being dealt, standard action bets being taken, and the side pots being grouped!

Happy coding, and good luck at the tables!

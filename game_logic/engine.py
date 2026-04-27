import random

def get_result(user_choice):
    options = ["stone", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    # Normalize user input
    user_choice = user_choice.lower().strip()
    
    if user_choice == computer_choice:
        return f"It's a tie! Both chose {computer_choice.capitalize()}."

    # Rules of the game
    win_map = {
        "stone": "scissors",
        "paper": "stone",
        "scissors": "paper"
    }

    if win_map.get(user_choice) == computer_choice:
        return f"✨ You win! Computer chose {computer_choice.capitalize()}."
    else:
        return f"🤖 Computer wins! Computer chose {computer_choice.capitalize()}."
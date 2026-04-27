import random

def get_result(user_choice):
    option = ["stone", "paper", "scissors"]
    computer_choice = random.choice(option)
    
    user_choice = user_choice.lower().strip()
    
    if user_choice == computer_choice:
        return f"It's a tie! Both choose {computer_choice}."

    win= {
        "stone": "scissors",
        "paper": "stone",
        "scissors": "paper"
    }

    if win.get(user_choice) == computer_choice:
        return f"You win! Computer chose {computer_choice}."
    else:
        return f"Computer wins! Computer chose {computer_choice}."
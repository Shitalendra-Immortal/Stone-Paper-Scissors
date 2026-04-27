from game_logic.engine import get_result

def main_menu():
    while True:
        print("\n==========================")
        print("  STONE PAPER SCISSORS  ")
        print("==========================")
        print("1. Play Round")
        print("2. Exit")
        
        choice = input("\nSelect an option (1-2): ")
        
        if choice == "1":
            move = input("Enter Stone, Paper, or Scissors: ")
            
            
            if move.lower() in ["stone", "paper", "scissors"]:
                result = get_result(move)
                print(f"\nRESULT: {result}")
            else:
                print("\n Invalid choice! Please type Stone, Paper, or Scissors.")
                
        elif choice == "2":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid selection. Please choose 1 or 2.")

main_menu()
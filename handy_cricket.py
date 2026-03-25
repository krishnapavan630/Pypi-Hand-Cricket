import random

# Helper for safe integer input with prompt and range check
def get_int_input(prompt, valid_range=None):
    while True:
        try:
            val = input(prompt)
            if val.strip() == '':
                print("Please enter a number!")
                continue
            num = int(val)
            if valid_range and num not in valid_range:
                print(f"Please enter a number between {valid_range.start} and {valid_range.stop - 1}!")
                continue
            return num
        except ValueError:
            print("That's not a valid number. Try again!")
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Goodbye!")
            exit()


def user_batting():
    print("\n🎮 You are Batting! Time to score big! 🎮\n")
    user_runs = 0
    print("Pick a number between 1 and 6 for each ball. Let's play!\n")
    while True:
        comp = random.randint(1, 6)
        user = get_int_input("Your shot (1-6): ", range(1, 7))
        print(f"Computer bowls: {comp}")
        if comp == user:
            print("💥 Oh no, you're OUT! 💥")
            print(f"Your final score: {user_runs}\n")
            break
        user_runs += user
        print(f"Nice! Your total: {user_runs}\n")
    comp_runs = 0
    print(f"Computer needs {user_runs + 1} runs to win. Can you defend it?\n")
    print("Now you are Bowling!\n")
    while True:
        comp = random.randint(1, 6)
        user = get_int_input("Your bowl (1-6): ", range(1, 7))
        print(f"Computer hits: {comp}")
        if comp == user:
            print("🔥 You got the computer OUT! 🔥")
            print(f"Computer's final score: {comp_runs}\n")
            break
        comp_runs += comp
        print(f"Computer's total: {comp_runs}\n")
        if comp_runs > user_runs:
            break
    if comp_runs > user_runs:
        print(f"😢 Computer wins by {comp_runs - user_runs} runs. Better luck next time!")
    elif comp_runs < user_runs:
        print(f"🎉 You win by {user_runs - comp_runs} runs! Congratulations! 🎉")
    else:
        print("🤝 It's a TIE! What a close match!")


def comp_batting():
    print("\n🕹️ Computer is Batting! Can you bowl it out? 🕹️\n")
    comp_runs = 0
    while True:
        comp = random.randint(1, 6)
        user = get_int_input("Your bowl (1-6): ", range(1, 7))
        print(f"Computer hits: {comp}")
        if comp == user:
            print("🔥 You got the computer OUT! 🔥")
            print(f"Computer's final score: {comp_runs}\n")
            break
        comp_runs += comp
        print(f"Computer's total: {comp_runs}\n")
    print(f"You need {comp_runs + 1} runs to win. Time to bat!\n")
    user_runs = 0
    while True:
        comp = random.randint(1, 6)
        user = get_int_input("Your shot (1-6): ", range(1, 7))
        print(f"Computer bowls: {comp}")
        if comp == user:
            print("💥 Oh no, you're OUT! 💥")
            print(f"Your final score: {user_runs}\n")
            break
        user_runs += user
        print(f"Nice! Your total: {user_runs}\n")
        if user_runs > comp_runs:
            break
    if comp_runs > user_runs:
        print(f"😢 Computer wins by {comp_runs - user_runs} runs. Better luck next time!")
    elif comp_runs < user_runs:
        print(f"🎉 You win by {user_runs - comp_runs} runs! Congratulations! 🎉")
    else:
        print("🤝 It's a TIE! What a close match!")


def toss_win():
    print("🏆 You won the toss!")
    while True:
        print("Choose your option:\n1) Batting\n2) Bowling")
        opt = get_int_input("Enter 1 for Batting or 2 for Bowling: ", range(1, 3))
        if opt == 1:
            user_batting()
            break
        elif opt == 2:
            comp_batting()
            break
        else:
            print("Invalid option. Try again!")


def toss_lost():
    print("😬 You lost the toss!")
    choices = ['Batting', 'Bowling']
    comp_p = random.choice(choices)
    print(f"Computer chooses to {comp_p.lower()} first!")
    if comp_p == 'Batting':
        comp_batting()
    else:
        user_batting()


def toss(opt):
    if opt == 1:
        print("\nYou chose Even for the toss.")
    else:
        print("\nYou chose Odd for the toss.")
    user_toss_val = get_int_input("Enter your toss number (1-6): ", range(1, 7))
    comp_toss_val = random.randint(1, 6)
    print(f"Computer picks: {comp_toss_val}")
    total = user_toss_val + comp_toss_val
    print(f"Toss total: {total} ({'Even' if total % 2 == 0 else 'Odd'})")
    if (opt == 1 and total % 2 == 0) or (opt == 2 and total % 2 != 0):
        toss_win()
    else:
        toss_lost()


def start_game():
    while True:
        print("\n🌟 Let's start the Hand Cricket game! 🌟\n1) Even (for toss)\n2) Odd (for toss)\n3) Go back\n")
        opt = get_int_input("Choose an option (1-3): ", range(1, 4))
        if opt in [1, 2]:
            toss(opt)
            break
        elif opt == 3:
            print("See you next time! Returning to main menu.\n")
            break
        else:
            print("Invalid option. Try again!")


def show_instructions():
    print('''\n📖 How to Play Hand Cricket 📖\n\n1. The game starts with a toss. Choose Even or Odd and pick a number (1-6).\n2. If you win the toss, choose to bat or bowl first.\n3. When batting, pick a number (1-6) each ball. If the computer picks the same, you're OUT!\n4. When bowling, try to match the computer's number to get it OUT.\n5. After the first innings, roles switch. The chaser must beat the target to win.\n6. Have fun and play fair!\n''')


def main():
    while True:
        print('''\n🏏 Welcome to Hand Cricket Academy! 🏏\n--------------------------------------\n1) Start the game\n2) How to play\n3) Exit\n''')
        opt = get_int_input("Choose an option (1-3): ", range(1, 4))
        if opt == 1:
            start_game()
        elif opt == 2:
            show_instructions()
        elif opt == 3:
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
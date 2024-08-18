import random

def user_batting():
  print("\n################################ You are Batting ################################\n")
  user_runs=0
  print("********************************************Choose only the numbers between 1 to 6********************************************\n")
  while True:
    comp=random.randint(1,6)
    try:
      user=int(input("Enter your runs from 1 to 6 Bat : "))
      print("Computer bowls",comp)
      if (comp==user):
        print("................................... OUT ...................................")
        print("Your score: ",user_runs)
        break
      if user not in [1,2,3,4,5,6] :
        print("Invalid input. Try Again")
        continue
      user_runs=user_runs+user
    except ValueError:
      print("Invalid input. Try Again")
      continue
  comp_runs=0
  print(f"Computer requires {user_runs+1} to win the game")
  print("\n################################ You are Bowling ################################\n")
  print("******************************************** Choose only the numbers between 1 to 6 ********************************************\n")
  while True:
      comp=random.randint(1,6)
      try:
        user=int(input("Choose a number for bowling: "))
        print("Computer runs",comp)
        if (comp==user):
          print("................................... OUT YOU HAVE DISMISSED THE COMPUTER ...................................")
          print("Computer score: ",comp_runs)
          break
        if user not in [1,2,3,4,5,6]:
          print("Invalid input. Try again")
          continue
        comp_runs=comp_runs+comp
      except ValueError:
        print("Invalid input. Try Again")
        continue
      if (comp_runs>user_runs):
                break
  if (comp_runs>user_runs):
    print("Computer runs : ",comp_runs)
    print("You lost the game")

  elif(comp_runs<user_runs):
    print("HURRAY you won by",((user_runs)-(comp_runs)),"runs,congratulations...!")

  else:
    print("TIE MATCH")

def comp_batting():
  print("\n################################ You are Bowling ################################\n")
  print("************************************************* Computer is ready for batting *************************************************\n")
  comp_runs=0
  while(True):
    comp=random.randint(1,6)
    try:
      user=int(input("Choose a number for bowling: "))
      print("Computer runs",comp)
      if (comp==user):
        print("................................... OUT YOU HAVE DISMISSED THE COMPUTER ...................................\n")
        print("Computer score : ",comp_runs)
        break
      if user not in [1,2,3,4,5,6]:
        print("Invalid input. Try Again")
        continue
      comp_runs=comp_runs+comp
    except ValueError:
      print("Invalid input. Try Again")
      continue
  print(f"You require {comp_runs+1} runs to win the game\n")
  print("\n################################ You are Batting ################################\n")
  print("******************************************** Choose only the numbers between 1 to 6 ********************************************\n")
  user_runs=0
  while(True):
    comp=random.randint(1,6)
    try:
      user=int(input("enter your runs from 1 to 6 Bat : "))
      print("computer bowls",comp)
      if (comp==user):
        print("You are out")
        print("YOUR SCORE : ",user_runs)
        break
      if user not in [1,2,3,4,5,6]:
        print("invalid input...\n game restarting")
        continue
      user_runs=user_runs+user
    except ValueError:
      print("Invalid input. Try Again")
      continue
    if (user_runs>comp_runs):
      break
  if (comp_runs>user_runs):
    print("computer runs : ",comp_runs)
    print("you lost the game")
  elif (comp_runs<user_runs):
    print("HURRAY you won the by",((user_runs)-(comp_runs)),"runs,congratulations...!")
  else:
    print("TIE MATCH")


def toss_win():
    print("You have won the toss")
    print('''Select your option:
1) Batting
2) Bowling''')
    try:
        opt = int(input("Choose Batting or Bowling: "))
        if opt == 1:
            user_batting()
        elif opt == 2:
            comp_batting()
        else:
            print("\nInvalid option. Please try again.")
            toss_win()
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
        toss_win()

def toss_lost():
    print("Oops, you have lost the toss")
    choices = ['Batting', 'Bowling']
    comp_p = random.choice(choices)
    print(f"Computer choses to {comp_p}")
    if comp_p == 'Batting':
        comp_batting()
    else:
        user_batting()

def toss(opt):
    if opt == 1:
        print("\nYou have selected Even")
        try:
            user_toss_val = int(input("Enter your number: "))
            comp_toss_val = random.randint(1, 6)
            print(f"The computer has chosen {comp_toss_val}")
            if (user_toss_val + comp_toss_val) % 2 == 0:
                toss_win()
            else:
                toss_lost()
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            toss(opt)
    elif opt == 2:
        print("\nYou have selected Odd")
        try:
            user_toss_val = int(input("Enter your number: "))
            comp_toss_val = random.randint(1, 6)
            print(f"The computer has chosen {comp_toss_val}")
            if (user_toss_val + comp_toss_val) % 2 != 0:
                toss_win()
            else:
                toss_lost()
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            toss(opt)

def start_game():
    print('''\n****************************** The game has just started ******************************
Select your option:
1) Even
2) Odd
3) Go to previous page \n''')
    try:
        opt = int(input("Enter your option: "))
        if opt == 1 or opt == 2:
            toss(opt)
        elif opt == 3:
            print("\nHope you come back.")
        else:
            print("\nInvalid option. Please try again.")
            start_game()
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        start_game()

def show_instructions():
    print('''\n
****************************** Instructions on how to play the game ******************************
************************************************************************************************************

Welcome to the Hand Cricket game, a fun 2-player game where you compete against the computer. Follow these steps to get started:

Toss and Selection:

The game begins with a toss. You will choose either "Even" or "Odd".
The computer will also select a number randomly.
If the sum of both numbers matches your choice of "Even" or "Odd", you win the toss and get to choose whether to bat or bowl.

Playing the Game:

Once you have chosen to bat or bowl, the game proceeds accordingly.
If you choose to bat, your goal is to score runs until you are dismissed.
If you choose to bowl, your aim is to dismiss the batsman while conceding as few runs as possible.
After the first innings, the roles switch: the previous bowler becomes the new batsman, and the new batsman must surpass the score set by the previous batsman to win.
Enjoy the game and may the best player win!
    ''')

def main():
    while True:
        print('''\n****************************** Welcome to Krishna Pavan Hand Cricket Academy ******************************
************************************************************************************************************
Select your option:
1) Start the game
2) How to play
3) Exit\n
''')
        try:
            opt = int(input())
            if opt == 1:
                start_game()
            elif opt == 2:
                show_instructions()
            elif opt == 3:
                print("\nExiting the game. Goodbye!")
                break
            else:
                print("\nInvalid option. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
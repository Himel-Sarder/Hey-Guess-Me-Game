from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
MEDI_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess != answer and abs(guess - answer) <= 10:

      print("You're very close!")
  if guess > answer:

    print("Too high.")
    return turns - 1
  elif guess < answer:

    print("Too low.")
    return turns - 1
  else:
    print()
    print(f"Congratulations !! You got Me! I am {answer}.")
    print()

#Make function to set difficulty.
def set_difficulty():
    """Set the difficulty level."""
    while True:
        level = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ").lower()
        if level in ['easy', 'medium', 'hard']:
            break
        else:
            print()
            print("Invalid input! Please choose 'easy', 'medium', or 'hard'.")
            print()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "medium":
        return MEDI_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play_again():
    """Ask the user if they want to play again and return True or False."""
    while True:
        play = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play in ['yes', 'no']:
            break
        else:
            print("Invalid input! Please type 'yes' or 'no'.")
    return play == 'yes'
def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print()
  print("Hey dear ! I'm within 1 and 100.")
  print()
  answer = randint(1, 100)
  #print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print("----------------------------------------------------------")
    print(f"You have {turns} attempts remaining to guess Me.")
    print("----------------------------------------------------------")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))
    print()

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print()
      print("You've run out of guesses, you lose.")
      print(f"I am {answer} !")
      return
    elif guess != answer:
      print()
      print("Guess again.")
      print()


game()
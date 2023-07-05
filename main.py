from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function definitions

# Compares answer to guess
def check_answer(guess, answer, turns):
  """Compares guess to answer, and returns the number of remaining turns"""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You win! The answer was {answer}!")

# Easy mode (10 guesses) or hard mode (5 guesses)
def mode_select():
  """Sets game difficulty"""
  level = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
  if level =="easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    
def game():  
  print(logo)
  print("\n\n")
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  # Computer generates answer
  answer = randint(1 , 100)
  # User guesses number in while loop
  turns = mode_select()
  
  guess = 0
  while guess != answer:
    if turns > 1:
      print(f"You have {turns} guesses left.")
    elif turns == 1:
      print(f"Careful, you only have {turns} guess left!")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print(f"You have run out of guesses and lose. Answer was {answer}.")
      return
  return
game()

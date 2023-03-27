"""EX05- Choose Your Own Adventure!"""

__author__ = "730313069"


points: int = 0

player_name: str = ""

import random


def greet() -> None:  # greet player and get their name
  global player_name
  print("Let's play COMPpet! The original COMP 110 pet game. Choose your pet, feed them snacks, and play with them to increase your points! ")
  player_name = input("First off, What is your name? ")
  print(f"Nice to meet you {player_name}! Let's go to the adoption center to choose your pet! ")
  return None


DOG_EMOJI: str = "\U0001F436"
CAT_EMOJI: str = "\U0001F431"
TURTLE_EMOJI: str = "\U0001F422"
MONKEY_EMOJI: str = "\U0001F412"
def adoption() -> None:  # custom procedure to choose pet
  global player_name
  print(f"Welcome to the adoption center, {player_name}. It is time to choose your pet. Below are the animals available for adoption! Choose your forever friend wisely.")
  print(f"Dog- {DOG_EMOJI}   Cat- {CAT_EMOJI}   Turtle- {TURTLE_EMOJI}   Monkey- {MONKEY_EMOJI} ")
  pet_choice: str = input("Which pet would you like to adopt? Choose dog, cat, turtle, or monkey. ")
  while pet_choice != "dog" and pet_choice != "cat" and pet_choice != "turtle" and pet_choice != "monkey":
    pet_choice = input("I'm sorry! We do not have that pet at our adoption center. Please choose between dog, cat, turtle, or monkey. ")
  else:
    pet_name: str = input(f"Wonderful choice, {player_name}! What would you like to name your new {pet_choice}? ")
    print(f"Cute! Lets take {pet_name} home. You earned 10 points and your pet's happiness increased by 5!")
    global points
    points += 10
  pet_emoji: str = ""
  if pet_choice == "dog":
    pet_emoji += DOG_EMOJI
  if pet_choice == "cat":
    pet_emoji += CAT_EMOJI
  if pet_choice == "turtle":
    pet_emoji == TURTLE_EMOJI
  if pet_choice == "monkey":
    pet_emoji == MONKEY_EMOJI
  at_home(pet_name, pet_emoji)
  return None


def at_home(pet_name: str, pet_emoji: str) -> None:
  global points
  print("====================== At Home \U0001F3E0 ==============================")
  print(f"Welcome home, {player_name} and {pet_name}. At home you can feed your pet and play games to increase their happiness points")
  happiness_points: int = 5
  print(f"This is {pet_name}'s current happiness points: {pet_emoji} {happiness_points} ")
  print("In order to feed your pet snacks and increase their happiness, you can pay 1 point.")
  print("Taking your pet on a walk will earn you 3 points and your pet 10 points happiness.")
  choices: list[str] = ['feed', 'walk', 'quit']
  activity_choice: str = input(f"What would you like to do with {pet_name} {pet_emoji} (feed, walk or quit)? ")
  while True:
    while activity_choice not in choices:
      print("Invalid choice, please choose again. ")
      activity_choice = input("feed, walk or quit: ")
    if activity_choice == "feed":
      print(f"Yay! You gave {pet_name} a treat! Their happiness increased 3 points. You spent 1 adventure point on the treat. ")
      points -= 1
      happiness_points += 3
    elif activity_choice == "walk":
      print(f"Yay! This walk with {pet_name} is awesome! Both of your points have increased!")
      points += 3
      happiness_points += 5
    play_again: str = input("Do you want to keep playing? Enter 'yes' or 'no': ")
    if play_again == 'no':
      break
  print(f"Time to leave home! Currently you have {points} adventure points and {pet_name} has {happiness_points} happiness points. ")
  return None
  

def play_function(points) -> int:
  """Play games with your pet in order to earn more points."""
  global player_name
  print("=============Mini Game=================")
  print(f"Hey {player_name}, Let's play a game to earn adventure points!")
  print(f"In this mini-game, you will try to guess what toy your pet wants; ball, plushie, or bone.")
  print(f"If you correctly guess what toy your pet wants, you will earn 5 adventure points.")
  toys: list[str] = ['ball', 'plushie', 'toy']
  random_toy: str = random.choice(toys)
  guess: str = input(f"Okay, {player_name}, Make your choice: ")
  if guess == random_toy:
    print(f"Nice work, {player_name}, You guessed right! ")
    points += 5
  else:
    print("I'm sorry that is not correct! Come back for another mini game soon.")
  print(f"You now have {points} points!")
  return points


def main() -> None:
  greet()
  adoption()
  print("Do you want to continue playing? ")
  choice: str = input("Press 'y' to continue, or any other key to quit. ")
  while choice == "y":
    adventure_choice: str = input("Press 'a' to go back to the adoption center, or 'b' to play a mini game! ")
    if adventure_choice == "a":
      adoption()
    else:
      global points
      points = play_function(points)
  else:   
    print(f"Goodbye {player_name}, You earned {points} adventure points. ")
  return None


if __name__ == "__main__":
  main()
    
    

  

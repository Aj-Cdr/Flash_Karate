# i made some weird changes 

import random
import time

game_active = True
high_score = 0

print("""Welcome to the Karate Stance Flashcard Game! 
Test your knowledge of karate stances.
Get ready to punch and kick your way to a high score!""")

flashcards = {
    "Shezentai": "Natural Stance",
    "Choku-Zuki": "Straight Punch",
    "Oi-Zuki": "Front Lunge Punch",
    "Gyaku-Zuki": "Reverse Punch",
    "Gedan Barai": "Down Block",
    "Age-Uke": "Rising Block"
}
keys = list(flashcards.keys())

while game_active:
    random.shuffle(keys)

    correct_guesses = 0
    total_points = 0

    for key in keys:
        start_time = time.time()
        user_guess = input(f'\nSensei says: What does {key} mean? ')
        end_time = time.time()
        elapsed_time = end_time - start_time

        if user_guess.lower() == flashcards[key].lower():
            correct_guesses += 1
            points = int(10 - elapsed_time)  # Calculate points based on elapsed time
            points = max(points, 10)
            total_points += points
            print(f"Great job! You got it right and earned {points} points.", "\n")
        else:
            print("Hmm, not quite! The correct definition was ", flashcards[key], "\n")

    print("You earned ", total_points, " points!\n")
  
    percent = int(correct_guesses / len(keys))
    
    if percent == 100:
      print(
        "Wow, a perfect score, one hundred percent! You are a karate master!")
    elif percent >= 80:
      print(
        f"Excellent job, you recieved a {percent}% score from Sensei! You know your stuff."
      )
    elif percent >= 60:
      print(
        f"Good work, you got a {percent}% score! Keep practising your stances.")
    else:
      print(
        f"You completely failed this class with a {percent} percent. There's not next time for you to try again. You're expelled!"
      )

    if total_points > high_score:
        high_score = total_points
        print("Congratulations! You achieved a new high score!")
    print(f"Your current high score is {high_score}")

    play_again = input("Play again? [Y/N]: ")
    print('_' * 25, '\n')

    if play_again != "Y":
        game_active = False

print("Thanks for playing the Karate Stance Flashcards Game! Keep training hard.")

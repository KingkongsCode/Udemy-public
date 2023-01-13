from art import logo, vs
from game_data import data
import random
import os

# generera en random int
# ta ut en dictionary från data 
def random_celeberty():
    num = random.randint(0, 49)
    return data[num]

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


compare = random_celeberty()
against = random_celeberty()
correct_answer = True
score = 0
while correct_answer is not False:
    print(logo)
    if score >= 1:
        print(f"Correct, current score: {score}")
    compare_name = compare["name"]
    compare_followers = compare["follower_count"]
  
    compare_desc = compare["description"]
    compare_country = compare["country"]

    print(f"Compare A: {compare_name}, a {compare_desc}, from {compare_country}")


    print(vs)
    against_name = against["name"]
    against_followers = against["follower_count"]
    
    against_desc = against["description"]
    against_country = against["country"]

    print(f"Against B: {against_name}, a {against_desc}, from {against_country}")
    
    option = input("Who has more followers? Type 'A' or 'B': ").lower()


    if option == "a" and compare_followers > against_followers:
        against = random_celeberty()
        score += 1
        clearConsole()
    elif option == "b" and compare_followers < against_followers:
        compare = against
        against = random_celeberty()
        score += 1
        clearConsole()
    else:
        clearConsole()
        print(f"Sorry that is not correct. Final score was: {score} ")
        correct_answer = False
    

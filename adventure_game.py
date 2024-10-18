import random
import time
import sys

# Function to print a message and pause for 2 seconds
def print_pause(t):
    print(t)
    time.sleep(2)

total_score = 0

# Function to calculate the total score
def calculate_score(points):
    global total_score
    total_score += points

def cave_scenario():
    # Player enters the dark cave and meets a dragon
    print_pause("You bravely enter the dark cave, your weapon at the ready.")
    calculate_score(20)
    print("Now, there is a dragon in front of you :0")
    print("Run or Fight?")
    dis = input("Enter your dis (3 or 4): ")
    if dis == "3":
        # Player runs away to the waterfall
        print_pause("If you're afraid like a child, rush straight to the waterfall sound.")
        print_pause("Fearful guy, run to the right path to find the waterfall")
        water_sound_scenario()
        calculate_score(25)
    elif dis == "4":
        # Player battles the dragon
        print_pause("You're too brave. I'll give you a hint.")
        print("\033[1;31mDragon allergic to their eyes\033[0m")
        print_pause("for your brave, I'll give you a weapon to help you in front of this dragon")
        time.sleep(3)
        weapons = ['Dragon bones Arrows', 'Storm Blade', 'Thunder Hammer']
        current_weapon = random.choice(weapons)
        print(current_weapon)
        time.sleep(3)
        print("WOW! You're a great fighter!")
        print_pause("You killed the dragon!")
        print_pause("Now you reached the end of the game")
        calculate_score(100)

def water_sound_scenario():
    # Player follows the sound of water and reaches a waterfall
    print_pause("You follow the sound of the water and arrive at a beautiful waterfall.")
    print("You see a path leading up the waterfall and a hidden door behind it.")
    
    while True:
        print_pause("Enter 1 to climb up the waterfall path.")
        print_pause("Enter 2 to open the hidden door.")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            # Player climbs the waterfall path and finds treasure
            print_pause("You climb up the waterfall path and discover a hidden treasure!")
            calculate_score(30)
            print_pause("Congrats! You found the treasure. You reached the end of the game.")
            calculate_score(60)
            break  # Break out of the loop after valid input
        elif choice == "2":
            # Player opens the hidden door and enters a maze
            print_pause("You open the hidden door and find yourself in a maze.")
            print_pause("Navigate through the maze to find the exit.")
            calculate_score(50)
            print_pause("You find the exit. That's the end of the game.")
            calculate_score(30)
            break  # Break out of the loop after valid input
        else:
            print_pause("Invalid choice. You are still standing, choose your next move.")

def play_game():
    while True:
        print("Your current score is:", total_score)

        if total_score >= 100:
            print("Congratulations! You win the game!")
            break

        elif total_score < 0:
            print("Game over! You lose.")
            break

        print_pause("As you make your way deep into the mystical forest, you come to a crossroad in the trail.")
        print_pause("To your left, you notice a darkly shown cave opening.")
        print_pause("To your right, the sound of water flowing can be heard.")
        print_pause("Enter 1 to go into the dark cave.")
        print_pause("Enter 2 to investigate the source of the sound.")

        while True:
            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                cave_scenario()
                break  # Break out of the loop after valid input
            elif choice == "2":
                water_sound_scenario()
                break  # Break out of the loop after valid input
            else:
                print_pause("Invalid choice. Please enter '1' or '2'.")

        a = input("Do you want to continue playing? (yes or no): ")

        if a == "no":
            print("Maybe next time. Goodbye!")
            break

        elif a != "yes":
            print("Invalid choice. Please try again.")

    end_game()

def end_game():
    print("Final score:", total_score)
    sys.exit()

def start_game():
    print("Congratulations! This is the Phoenix Sea Swords game")
    time.sleep(2)

    while True:
        a = input("Do you want to play? (yes or no): ")

        if a == "yes":
            print("Now you are in a mystical forest")
            print("I'll give you some tools to help you on your way")
            time.sleep(1)
            print("Dragon sword, Bird bomb, Butterfly knife")
            weapons = input("CHOOSE YOUR WEAPON: ")

            if weapons == "Dragon sword":
                print("Great choice")
            elif weapons == "Bird bomb":
                print("Oooh, you are too brave")
            elif weapons == "Butterfly knife":
                print("You look cute or dumb")
            else:
                print("Invalid weapon choice. You will proceed without a weapon.")

            time.sleep(1)
            print("You can begin your adventure now")
            play_game()

            # After the game ends, ask the player to restart or exit
            choice = ""
            while choice != "restart" and choice != "exit":
                choice = input("Game over! Do you want to restart or exit? Enter 'restart' to play again or 'exit' to quit: ")
                if choice != "restart" and choice != "exit":
                    print("Invalid choice. Please enter 'restart' or 'exit'.")

            if choice == "restart":
                total_score = 0  # Reset the score
                continue  # Restart the game

            elif choice == "exit":
                print("Maybe next time. Goodbye!")
                end_game()

        elif a == "no":
            # Player chooses to quit the game
            print("Maybe next time. Goodbye!")
            end_game()

        else:
            print("Invalid choice. Please try again.")

start_game()

# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 4 - Problem 3
# This program write a method in Python to write multiple lines of text contents into a text file.

import time
import pyfiglet
from colorama import Fore, Back, Style
from tqdm import tqdm

def intro():
    # display heading output
    print("")
    heading = pyfiglet.figlet_format("WRITTEN MULTIPLE TEXT LINES", font="3-d", width=90)
    print(Style.BRIGHT + Fore.CYAN + heading)

    # create introductory message
    intro = "Input any word or phrase.\n"
    intro += f"{Fore.GREEN}\nEnter 'y' to continue.{Style.RESET_ALL}"
    intro += f"{Fore.RED}\nEnter 'n' to terminate.{Style.RESET_ALL}\n"
    print(intro)
    time.sleep(1.5)

def main():
    # open the mylife.txt in write mode
    with open("mylife.txt", "w") as input_file:
        
        # use looping to keep asking the user for input
        while True:
            # ask the user for input
            user_input = input(f"{Fore.YELLOW}Enter line:{Style.RESET_ALL} ")
            
            # write the input to the file
            input_file.write("Enter line: " + str(user_input + "\n"))
            
            # ask the user if they want to add more lines
            conditional = input(Fore.GREEN + "\033[1mAre there more lines (y/n)?  \033[0m" + Fore.YELLOW)
            
            # write the input to mylife.txt
            input_file.write("Are there more lines (y/n)? " + str(conditional) + "\n")
            
            # if user input is yes
            if conditional.lower().strip() == "y":
                continue
            
            # if user input is no
            elif conditional.lower().strip() == "n":
                time.sleep(1)
                print(Fore.CYAN + "\n[Exiting program in...] \n")
                for i in range(3, 0, -1):
                    print(f"{Fore.CYAN}{Back.WHITE}{Style.BRIGHT}{i}{Style.RESET_ALL}")
                break
    
    # print progress bar while writing to the file
    print(Fore.YELLOW + "\nSaving to file...\n")
    for i in tqdm(range(100)):
        time.sleep(0.01)

    time.sleep(2)
    print(Fore.GREEN + "\n[File saved successfully!]\n")

def outro():
    print(" ")
    header = pyfiglet.figlet_format("THANK YOU! GOODBYE!", font="banner3-D", width=90)
    print(Style.BRIGHT + Fore.GREEN + header)

if __name__ == '__main__':
    intro()
    main()
    outro()

    #testing
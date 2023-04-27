# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 4 - Problem 3
# This program write a method in Python to write multiple lines of text contents into a text file.

def main():
    # open the mylife.txt in write mode
    with open("mylife.txt", "w") as input_file:
        
        # use looping to keep asking the user for input
        while True:
            # ask the user for input
            user_input = input("Enter line: ")
            
            # write the input to the file
            input_file.write("Enter line: " + str(user_input + "\n"))
            
            # ask the user if they want to add more lines
            conditional = input("Are there more lines (y/n)? ")
            
            # write the input to mylife.txt
            input_file.write("Are there more line (y/n)? " + str(conditional) + "\n")
            
            # if user input is yes
            if conditional.lower().strip() == "y":
                continue
            
            # if user input is no
            elif conditional.lower().strip() == "n":
                time.sleep(1)
                print("\n[Exiting program...] \n")
                break
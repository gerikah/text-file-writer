# Object Oriented Programming CMPE-103 PROGRAMMING EXERCISE: Problem 3
# ALDAY, Gerikah L. - BSCPE 1-5

import pyfiglet
border = "-" * 180
title = ("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("text file\nwriter\n", justify = "center", font = "isometric1", width = 175) + "\n")
print(title)

name = ("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("what is your name?\n", justify = "center", font = "cybermedium", width = 175) + "\n")
print(name)
input_name = input(" ".center(80))

def write_to_file():
    # open the file in write mode
    with open ("mylife.txt", "w") as my_file:

        # iterate until the user is done entering line        
        while True:

            border = "-" * 180
            
            # prompt the user to enter a line of text
            line = ("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("enter new line\n", justify = "center", font = "cybermedium", width = 175) + "\n")
            print(line)
            input_line = input(" ".center(80))

            
            # write the line to the file
            my_file.write(f"{border}\n\n{input_line}\n\n")

            # prompt the user to enter if there are more lines to enter
            new_line = ("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("are there more line,\n" + input_name + "? y/n" , justify = "center", font = "cybermedium", width = 175) + "\n")
            print(new_line)
            decision = input (" ".center(80))
            
            # if user input  is "y", continue
            if decision.lower() == "y":
                continue
            
            # if user input is "n", break the loop
            else:
                break

# close the file
    my_file.close()
write_to_file()

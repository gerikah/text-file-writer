
name = input("what is your name? ")

def write_to_file():
    # open the file in write mode
    with open("mylife.txt", "w") as my_file:
        # iterate until the user is done entering line
        while True:
            # prompt the user to enter a line of text
            line = input("enter line: ")
            # write the line to the file
            my_file.write (line + "\n")
            # prompt the user to enter if there are more lines to enter
    # read user input
    # if user input  is "y", continue
    # if user input is "n", break the loop
# close the file
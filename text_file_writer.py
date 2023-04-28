
name = input ("what is your name? ")

def write_to_file():
    # open the file in write mode
    with open ("mylife.txt", "w") as my_file:
        # iterate until the user is done entering line
        while True:
            # prompt the user to enter a line of text
            line = input ("enter line: ")
            # write the line to the file
            my_file.write (line + "\n")
            # prompt the user to enter if there are more lines to enter
            new_line = input (f"are there more lines, {name}? y/n ")
            # if user input  is "y", continue
            if new_line.lower() == "y":
                continue
            # if user input is "n", break the loop
            else:
                break
# close the file
    my_file.close()
write_to_file()
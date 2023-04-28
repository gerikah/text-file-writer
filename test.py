def write_to_file():
    name = input("What is your name? ")

    # open the file in append mode
    my_file = open("mylife.txt", "a")

    # write a permanent line to the file
    my_file.write("This is a permanent line that will always be in the file.\n")

    # iterate until the user is done entering lines
    while True:
        # prompt the user to enter a line of text
        line = input("Enter line: ")

        # write the line to the file
        my_file.write(line + "\n")

        # prompt the user to enter if there are more lines to enter
        new_line = input("Are there more lines, " + name + "? ")

        # if user input is "y", continue
        if new_line.lower() == "y":
            continue
        # if user input is "n", break the loop
        else:
            break

    # close the file
    my_file.close()

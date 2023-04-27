>>> TEXT-FILE-WRITER

This Python program allows the user to write multiple lines of text content into a text file named "mylife.txt".

> Prerequisites

Before running this program, you need to have Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/

> How to run the program

1. Clone the repository to your local machine.
2. Open the terminal/command prompt and navigate to the project directory.
3. Run the following command: "python text_file_writer.py"

> Description

This program prompts the user to enter multiple lines of text content that will be written to a text file named "mylife.txt". The program will continue to prompt the user to enter more lines until the user chooses to stop.

> Usage

When the program runs, it will prompt the user to enter the first line of text content. After entering the first line, the program will ask the user if they have more lines to enter. If the user answers "y" or "Y", the program will prompt the user to enter the next line. If the user answers "n" or "N", the program will stop prompting the user and will write the entered lines to a file named "mylife.txt".

> Examples

Example Input/Output

    ---
    Enter line: Beautiful is better than ugly.
    Are there more lines y/n ? y
    Enter line: Explicit is better than implicit.
    Are there more lines y/n ? y
    Enter line: Simple is better than complex.
    Are there more lines y/n ? n
    ---

In this example, the user enters three lines of text content. After entering the last line, the program stops prompting the user and writes the lines to a file named "mylife.txt".

Example Output

If you open the "mylife.txt" file after running the program with the above input, the file will contain the following text:

    ---
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    ---

> License

This project is licensed under the MIT License - see the LICENSE.md file for details.

> Acknowledgments

This program was created as part of a Python programming exercise in Object Oriented Programming
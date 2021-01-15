#!/usr/bin/python
import sys


# Define count_words(data) function that counts the number of words in data and returns the value.
def count_words(data):

    # Define words variable as list of words in the data file.
    words = data.split(" ")

    # Define num_words variable as the number of words in a list.
    num_words = len(words)

    return num_words


# Define count_line(data) function that counts the number of lines with text and returns that value.
def count_lines(data):

    # Define lines variable as a list of lines in the data file.
    lines = data.split("\n")

    # For loop that iterates over lines and removes lines without text.
    for current_line in lines:
        if not current_line:
            lines.remove(current_line)

    return len(lines)


if __name__ == "__main__":

    # If the number of arguments given is less than two print proper way to run tool.
    if len(sys.argv) < 2:
        print("Usage: python3 ./word_count.py ./<file>")
        exit(1)

    # Define filename variable as the name of 2nd argument given.
    filename = sys.argv[1]

    # open and read the given file defining data variable as data within the file.
    with open(filename, "r") as f:
        data = f.read()

    # call functions
    num_words = count_words(data)
    num_lines = count_lines(data)

    # print results
    print("The number of words: ", num_words)
    print("The number of lines: ", num_lines)

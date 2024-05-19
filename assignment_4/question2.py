# 2. Write a Python program to read a text file line by line and display the number of words in each line.
# Create a dome text file by it yourself for this assignment

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                words = line.split()
                num_words = len(words)
                print("line",line_num,"=",num_words,"words")
    except FileNotFoundError:
        print("File not found!")

filename = 'sample.txt'
count_words(filename)

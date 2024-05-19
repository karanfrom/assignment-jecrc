# 4. Write a Python program to find the longest word in a given list of words.
# If there are multiple words with the same length, return the first one encountered word.
def find_longest_word(words):
    if not words:
        return None

    longest_word = words[0]
    max_length = len(longest_word)

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word


word_list = ["apple", "banana", "orange", "grapefruit", "kiwi"]
longest_word = find_longest_word(word_list)
print("Longest word:", longest_word)

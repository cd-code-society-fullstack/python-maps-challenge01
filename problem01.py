def count_letter_frequency(data):
    frequency = {}

    for char in data:
        if char.isalpha():  # check if the character is a letter
            char = char.lower()  # convert the letter to lowercase
            if char not in frequency:
                frequency[char] = 1  # if the letter is not in the dictionary, add it
            else:
                frequency[char] += 1  # if the letter is already in the dictionary, increment its count

    return frequency

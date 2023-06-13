def count_duplicates(data):
    # Create a dictionary to store the frequency of each character
    freq = {}

    for char in data:
        # If the character is already in the dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            freq[char] = 1

    # Count the number of characters that appear more than once
    duplicates = 0
    for char, count in freq.items():
        if count > 1:
            duplicates += 1

    return duplicates



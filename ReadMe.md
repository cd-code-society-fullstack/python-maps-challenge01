## problem 01

**Problem Statement**

Given a string `data`, your task is to implement a function `countLetterFrequency` that counts the frequency of each letter in the string and returns an object. The object should have the letters as keys and the count of each letter as values. The letters should be converted to lowercase. Non-letter characters should be ignored.

The `countLetterFrequency` function should accept one parameter:

1. `data`: a string.

Here are some examples:

- `countLetterFrequency("aabAc")` should return `{ a: 3, b: 1, c: 1 }`, as 'a' appears thrice, 'b' appears once and 'c' appears once.

{Try It!}(python3 .guides/01/try-it-01.py)

- `countLetterFrequency("Hello there!")` should return `{ h: 2, e: 3, l: 2, o: 1, t: 1, r: 1 }`.

{Try It!}(python3 .guides/01/try-it-02.py)

- `countLetterFrequency("1234ab!!")` should return `{ a: 1, b: 1 }`.

{Try It!}(python3 .guides/01/try-it-03.py)

## Submit 

python3 .guides/secure/testRunner01.py

aabAc { 'a': 3, 'b': 1, 'c': 1 }
"Hello there!" { 'h': 2, 'e': 3, 'l': 2, 'o': 1, 't': 1, 'r': 1 }
1234ab!! { 'a': 1, 'b': 1 }
"AaBb123" {'a': 2, 'b': 2}

## Problem 02

**Problem Statement**

You are given a string. Your task is to implement a function named `count_duplicates` that counts the number of non-unique characters in the string.

The `count_duplicates` function should accept one parameter:
1. `data`: a string value.

Here are some examples:

- `count_duplicates("abcdefga")` should return `1`, as "a" is the only non-unique character.

{Try It!}(python3 .guides/02/try-it-01.py)

- `countDuplicates("xyzxyzxyz")` should return `3`, as "x", "y", and "z" each appear more than once.

{Try It!}(python3 .guides/02/try-it-02.py)

- `count_duplicates("aabbc")` should return `2`, as "a", "b", and "c" each appear more than once.

{Try It!}(python3 .guides/02/try-it-03.py)

**Hint**

Use a data structure to keep track of the occurrences of each character. Then count how many characters appear more than once.

## Submit 
python3 .guides/secure/testRunner02.py


# Test cases
abcdefga:1
xyzxyzxyz: 3
aabbc:2
PythonProgramming:2
HelloWorld:3

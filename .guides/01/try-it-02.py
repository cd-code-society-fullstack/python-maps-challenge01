import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem01 import count_letter_frequency

print(count_letter_frequency("Hello there!"))  # Expected: {'h': 2, 'e': 3, 'l': 2, 'o': 1, 't': 1, 'r': 1}

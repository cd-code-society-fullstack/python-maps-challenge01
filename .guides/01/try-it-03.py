import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem01 import count_letter_frequency

print(count_letter_frequency("1234ab!!"))  # Expected: {'a': 1, 'b': 1}




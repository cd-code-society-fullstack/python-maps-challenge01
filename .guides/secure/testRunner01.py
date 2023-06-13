import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem01 import count_letter_frequency

string = sys.argv[1]

print(count_letter_frequency(string)) 


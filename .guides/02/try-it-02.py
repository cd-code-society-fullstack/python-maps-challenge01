import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem02 import count_duplicates

print(count_duplicates("xyzxyzxyz"))

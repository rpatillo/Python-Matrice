#!/usr/bin/python
import sys
from pattern import pattern

def main(argv):
    pattern(argv[:-2], int(argv[-2]), int(argv[-1]))

if __name__ == "__main__":
    main(sys.argv[1:])
    

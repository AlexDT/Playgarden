#!/usr/bin/python

import sys

def main():
    int_number = 312
    print 'Name of this file:', sys.argv[0]
    print bin(int_number)
    print hex(int_number)
    print oct(int_number)

if __name__ == '__main__':
    main()

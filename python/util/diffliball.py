"""
Command line interface to difflib.py providing diffs in four formats:
"""
from __future__ import print_function
import sys
import difflib


def lines(filename):
    return open(filename).readlines()


def main():
    file1 = lines(sys.argv[1])
    file2 = lines(sys.argv[2])

    cdiff = difflib.Differ().compare(file1, file2)
    ndiff = difflib.ndiff(file1, file2)
    udiff = difflib.unified_diff(file1, file2)

    print ("file1:................................................")
    lineNum = 0
    for line in file1:
        lineNum+=1
        print ("%02d: %s" % (lineNum, line), end='')

    print ("file2:................................................")
    lineNum = 0
    for line in file2:
        lineNum+=1
        print ("%02d: %s" % (lineNum, line), end='')
    print ("cdiff: difflib.Differ().compare(file1, file2)................")
    lineNum = 0
    for line in cdiff:
        lineNum+=1
        print ("%02d: %s" % (lineNum, line), end='')
    print ("ndiff: difflib.ndiff(file1, file2)...........................")
    lineNum = 0
    for line in ndiff:
        lineNum += 1
        print ( "%02d: %s" % (lineNum, line), end='')
    print ("udiff: difflib.unified_diff(file1, file2)....................")
    lineNum = 0
    for line in udiff:
        lineNum += 1
        print ( "%02d: %s" % (lineNum, line), end='')

if __name__ == '__main__':
    main()

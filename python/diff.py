from __future__ import print_function
import sys
import optparse
import difflib


def lines(filename):
    return open(filename).readlines()


def main():
    usage = "usage: %prog fromfile tofile [-v] "
    parser = optparse.OptionParser(usage)
    parser.add_option("-v", action="store_true", default=False, help='verbose')
    (options, args) = parser.parse_args()
    if len(args) == 0:
        parser.print_help()
        sys.exit(1)
    if len(args) != 2:
        parser.error("need to specify both a fromfile and tofile")
    # file1, file2 = lines('../data/file1'), lines('../data/file2')
    file1, file2 = lines(sys.argv[1]), lines(sys.argv[2])
    ndiff = difflib.ndiff(file1, file2)
    defaultDiff = makeDefaultDiff(ndiff)
    if options.v:
        nDiffDump(file1, file2)
        defaultDiffDump(defaultDiff)
    printDefaultFormat(defaultDiff, file1, file2)


def nDiffDump(file1, file2):
    diff = difflib.ndiff(file1, file2)
    p0 = 0
    for line in diff:
        p0 += 1
        print ("%02d: %s" % (p0, line), end='')
    print ("")
    diff = difflib.ndiff(file1, file2)
    p0 = p1 = p2 = 0
    for line in diff:
        p0 +=1
        if line[:2] == "  ":
            p1 += 1
            p2 += 1
            continue
        elif line[:2] == "? ":
            continue
        elif line[:2] == "+ ":
            p2 += 1
        elif line[:2] == "- ":
            p1 += 1
        print ("%02d: %02d %02d %s" % (p0, p1, p2, line), end='')


def makeDefaultDiff(diff):
    defaultDiff = []
    triple = [set(), set(), set()]
    p0 = p1 = p2 = 0
    for line in diff:
        p0 +=1
        if line[:2] == "  ":
            p1 += 1
            p2 += 1
            continue
        elif line[:2] == "? ":
            continue
        elif line[:2] == "+ ":
            p2 += 1
        elif line[:2] == "- ":
            p1 += 1
        if triple[0] and p1 not in triple[1] and p2 not in triple[2]:
            defaultDiff.append(triple)
            triple = [set(), set(), set()]
        triple[0].add(line[:1])
        triple[1].add(p1)
        triple[2].add(p2)
    defaultDiff.append(triple)
    for line in defaultDiff:
        if len(line[0]) > 1:
            line[0] = set('c')
            line[2].remove(min(line[2]))
        elif line[0].pop() == '-':
            line[0].add('d')
        else:
            line[0].add('a')
        assert len(line[0]) == 1
        assert len(line[1]) >= 1
        assert len(line[2]) >= 1
    return defaultDiff


def defaultDiffDump(defaultDiff):
    print ("")
    p0 = 0
    for line in defaultDiff:
        p0 += 1
        print ("%02d: %s" % (p0, line), end='\n')


def printDefaultFormat(defaultDiff, file1, file2):
    p0 = 0
    for line in defaultDiff:
        p0 += 1
        op = list(line[0])[0]
        print (rangeFormat(line[1]) + op + rangeFormat(line[2]), end='\n')
        if op == 'd':
            for i in line[1]:
                print('<' + file1[i - 1], end='')
        elif op == 'a':
            for i in line[2]:
                print('>' + file2[i - 1], end='')
        elif op == 'c':
            for i in line[1]:
                print('<' + file1[i - 1], end='')
            print('---')
            for i in line[2]:
                print('>' + file2[i - 1], end='')


def rangeFormat(set):
    assert len(set) >= 1
    if len(set) == 1:
        return str(list(set)[0])
    else:
        return str(min(set)) + "," + str(max(set))

if __name__ == '__main__':
    main()

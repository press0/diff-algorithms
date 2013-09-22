""" 
A primitive alternative to difflib
based on https://gist.github.com/jorendorff/5040491
"""

from __future__ import print_function
import sys

def longest_matching_slice(a, a0, a1, b, b0, b1):
    sa, sb, n = a0, b0, 0
    runs = {}
    for i in range(a0, a1):
        new_runs = {}
        for j in range(b0, b1):
            if a[i] == b[j]:
                k = new_runs[j] = runs.get(j-1, 0) + 1
                if k > n:
                    sa, sb, n = i-k+1, j-k+1, k
        runs = new_runs
    assert a[sa:sa+n] == b[sb:sb+n]
    return sa, sb, n


def matching_slices(a, a0, a1, b, b0, b1):
    sa, sb, n = longest_matching_slice(a, a0, a1, b, b0, b1)
    if n == 0:
        return []
    return (matching_slices(a, a0, sa, b, b0, sb) + [(sa, sb, n)] +
            matching_slices(a, sa+n, a1, b, sb+n, b1))


def makeGenericDiff(a, b):
    diffGeneric = []
    ia = ib = 0
    slices = matching_slices(a, 0, len(a), b, 0, len(b))
    slices.append((len(a), len(b), 0))
    for sa, sb, n in slices:
        for line in a[ia:sa]:
            diffGeneric.append("- " + line)
        for line in b[ib:sb]:
            diffGeneric.append("+ " + line)
        for line in a[sa:sa+n]:
            diffGeneric.append("  " + line)
        ia = sa + n
        ib = sb + n
    return diffGeneric


def lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def rangeFormat(set):
    assert len(set) >= 1
    if len(set) == 1:
        return str(list(set)[0])
    else:
        return str(min(set)) + "," + str(max(set))


def printDefaultFormat(defaultDiff, file1, file2):
    p0 = 0
    for line in defaultDiff:
        p0 += 1
        op = list(line[0])[0]
        print (rangeFormat(line[1]) + op + rangeFormat(line[2]), end='\n')
        if op == 'd':
            for i in line[1]:
                print('<' + file1[i - 1], end='\n')
        elif op == 'a':
            for i in line[2]:
                print('>' + file2[i - 1], end='\n')
        elif op == 'c':
            for i in line[1]:
                print('<' + file1[i - 1], end='\n')
                print('---')
            for i in line[2]:
                    print('>' + file2[i - 1], end='\n')


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


if __name__ == '__main__':
    # file1, file2 = lines('../data/file1'), lines('../data/file2')
    file1, file2 = lines(sys.argv[1]), lines(sys.argv[2])
    genericDiff = makeGenericDiff(file1, file2)
    defaultDiff = makeDefaultDiff(genericDiff)
    printDefaultFormat(defaultDiff, file1, file2)

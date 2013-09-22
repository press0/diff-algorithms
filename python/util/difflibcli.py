""" Command line interface to difflib.py providing diffs in four formats:

* ndiff:    lists every line and highlights interline changes.
* context:  highlights clusters of changes in a before/after format.
* unified:  highlights clusters of changes in an inline format.
* html:     generates side by side comparison with change highlights.

"""

import sys
import optparse
import difflib


def main():
    usage = "usage: %prog [options] fromfile tofile"
    parser = optparse.OptionParser(usage)
    parser.add_option("-n", action="store_true", default=False, help='Produce a ndiff format diff (default)')
    parser.add_option("-c", action="store_true", default=False, help='Produce a context format diff')
    parser.add_option("-u", action="store_true", default=False, help='Produce a unified format diff')
    parser.add_option("-m", action="store_true", default=False, help='HTML side by side diff (can use with -c and -l)')
    parser.add_option("-l", "--lines", type="int", default=3,   help='Set number of context lines (default 3)')
    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.print_help()
        sys.exit(1)
    if len(args) != 2:
        parser.error("need to specify both a fromfile and tofile")

    n = options.lines

    if options.u:
        diff = difflib.unified_diff(lines(sys.argv[1]), lines(sys.argv[2]), n=n)
    elif options.c:
        diff = difflib.context_diff(lines(sys.argv[1]), lines(sys.argv[2]), n=n)
    elif options.m:
        diff = difflib.HtmlDiff().make_file(lines(sys.argv[1]), lines(sys.argv[2]), context=options.c, numlines=n)
    else:
        diff = difflib.ndiff(lines(sys.argv[1]), lines(sys.argv[2]))

    sys.stdout.writelines(diff)


def lines(filename):
    return open(filename).readlines()


if __name__ == '__main__':
    main()


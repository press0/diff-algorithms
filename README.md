#diff

diffing the diff algorithm *default format* - in c, perl, python, git

<b>c gnu diffutils</b>
[doc](http://www.gnu.org/software/diffutils/manual/diffutils.html#Detailed-Normal)
[source](https://github.com/press0/diff/blob/master/c/diffutils/src/diff.c)
``` 
Original Unix diff authored in C by Douglas McIlroy, James Hunt at Bell Labs, 1970s
Gnu version by Paul Eggert, Mike Haertel, David Hayes, Richard Stallman, Len Tower, 1980's
cloned from http://git.savannah.gnu.org/cgit/diffutils.git/
``` 


<b>perl Algorithm::Diff</b>
[doc](http://search.cpan.org/~tyemq/Algorithm-Diff-1.1902/lib/Algorithm/Diff.pm)
[source](http://cpansearch.perl.org/src/TYEMQ/Algorithm-Diff-1.1902/lib/Algorithm/Diff.pm)
``` 
Based on McIlroy-Hunt diff algorithm, 1970's
Authored by Ned Konz, perl@bike-nomad.com, 1980's
Adapted from the Smalltalk code of Mario I. Wolczko, <mario@wolczko.com>
Updates by Tye McQueen, http://perlmonks.org/?node=tye

implemented with STYLE => "OldStyle" 
```

<b>python difflib</b>
[doc](http://docs.python.org/2/library/difflib.html#difflib)
[source](http://hg.python.org/releasing/2.7.4/file/026ee0057e2d/Lib/difflib.py)
``` 
difflib based on Ratcliff-Obershelp algorithm, late 1980’s

implemented with and without difflib.  Transforms the context-free diff to default format
``` 

<b>git diff</b>
[doc](https://www.kernel.org/pub/software/scm/git/docs/git-diff.html)
[source](https://github.com/git/git)
``` 
 - prior to version 1.8.2.1, patience (BitTorrent protocol) and histogram algorithm options
 - after    version 1.8.2.1, patience, minimal, histogram, and myers (default) algorithm options
 - context format default
`- output begins with: 'diff --git'
 - delegates to external tools - git-diff-tool 
 `` 

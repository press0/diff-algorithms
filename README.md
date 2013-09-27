#diff

diff the diff algorithm _default format_ - in c, perl, python, svn, git


<b>c gnu diffutils</b>
[doc](http://www.gnu.org/software/diffutils/manual/diffutils.html#Detailed-Normal)
[source](http://git.savannah.gnu.org/cgit/diffutils.git/tree/src/diff.c)
[algorithm](http://www.xmailserver.org/diff2.pdf)
``` 
Original Unix diff authored by Douglas McIlroy, James Hunt at Bell Labs, 1970s
Gnu version authored by Paul Eggert, Mike Haertel, David Hayes, Richard Stallman, Len Tower, 1980's
Based on "An O(ND) Difference Algorithm and Its Variations" by Eugene Myers
``` 


<b>perl Algorithm::Diff</b>
[doc](http://search.cpan.org/~tyemq/Algorithm-Diff-1.1902/lib/Algorithm/Diff.pm)
[source](http://cpansearch.perl.org/src/TYEMQ/Algorithm-Diff-1.1902/lib/Algorithm/Diff.pm)
``` 
Based on McIlroy-Hunt diff algorithm
Authored by Ned Konz, perl@bike-nomad.com, 1980's
Adapted from the Smalltalk code of Mario I. Wolczko, <mario@wolczko.com>
Updates by Tye McQueen, http://perlmonks.org/?node=tye

implemented here with STYLE => "OldStyle" 
```

<b>python difflib</b>
[doc](http://docs.python.org/2/library/difflib.html#difflib)
[source](http://hg.python.org/releasing/2.7.4/file/026ee0057e2d/Lib/difflib.py)
``` 
Based on the Ratcliff-Obershelp algorithm, late 1980’s

implemented here with and without difflib. 
``` 

<b>svn diff</b>
[doc](http://svn.apache.org/repos/asf/subversion/trunk/subversion/libsvn_diff/lcs.c)
[source](http://svn.apache.org/repos/asf/subversion/trunk/subversion/libsvn_diff/lcs.c)
``` 
Based on "An O(NP) Sequence Comparison Algorithm", by Sun Wu, Udi Manber and Gene Meyers 
``` 

<b>git diff</b>
[doc](https://www.kernel.org/pub/software/scm/git/docs/git-diff.html)
[source](https://github.com/git/git)
``` 
before April 2013, patience (BitTorrent) and histogram algorithm options
after  April 2013, patience, histogram, and myers (default) algorithm options
context format default
output begins with: 'diff --git'
delegates to external tools - git-diff-tool 
``` 

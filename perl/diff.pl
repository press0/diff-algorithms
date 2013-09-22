#!/usr/bin/perl

use Text::Diff;
use strict;
use warnings;

my $diff = diff "$ARGV[0]", "$ARGV[1]", { STYLE => "OldStyle" };

print $diff;


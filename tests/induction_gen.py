#!/usr/bin/env python2

"""Generate a recursive induction example of given size; it makes rules
p(n+1) if p(n),q(n+1)
and
q(n+1) if p(n), q(n)
for n ranging in [0...size], and adds facts p(0) and q(0)"""

import sys

def generate(size):
    for i in xrange(size):
        print "p(n%d) :- p(n%d), q(n%d)." % (i+1, i, i+1)
        print "q(n%d) :- p(n%d), q(n%d)." % (i+1, i, i)
    print "p(n0)."
    print "q(n0)."

if __name__ == '__main__':
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print "%% generate problem of size %d" % size
    generate(size)


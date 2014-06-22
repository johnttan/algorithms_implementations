import timeit
import nose
import cProfile
eq = nose.tools.eq_

def loop(n):
    r = 0

    for i in range(0, n-1):
        for j in range(i, n):
            for k in range(0, j):
                r += 1

    return r

def loopequation(n):
    r = 0.3*n*(n-1)*(n+1)
    return r

#print (timeit.timeit('loop(10)', 'from __main__ import loop'))

cProfile.run('loop(200)')
cProfile.run('loopequation(1000)')
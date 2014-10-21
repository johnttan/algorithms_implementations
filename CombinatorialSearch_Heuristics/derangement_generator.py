__author__ = 'John Tan'
import nose
import timeit

eq = nose.tools.eq_

def subgen(possible, generated=[], i=1):
    if len(possible) > 0:
        for s in possible:
            if s != i:
                possible1 = list(possible)
                possible1.remove(s)
                generated1 = list(generated)
                generated1.append(s)
                return subgen(possible1, generated1, i+1)



def generate(possible):
    subgen(possible)



#generate([1, 2, 3, 4])
print(timeit.timeit('generate([1, 2, 3, 4, 5])', 'from __main__ import generate'))
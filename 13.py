https://www.hackerrank.com/challenges/defaultdict-tutorial/problem)

from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        print (" ".join( map(str,d[i]) ))
    else:
        print (-1)
		
		
		https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
		
		stu, marks = int(input()), input().split().index("MARKS")
print (sum([int(input().split()[marks]) for _ in range(stu)]) / stu)

https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
	
	https://www.hackerrank.com/challenges/word-order/problem
	
	from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))

https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

https://www.hackerrank.com/challenges/itertools-combinations/problem
from itertools import *

s,k = input().split(' ')

for l in range(1,int(k)+1):
    for c in combinations (sorted(s),l):
        print(''.join(c))
		
		https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
		
		from itertools import combinations_with_replacement as combs

s, k = input().split()
print(*[''.join(p) for p in combs(sorted(s), int(k))], sep='\n')

https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


https://www.hackerrank.com/challenges/hex-color-code/problem

import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]


https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')


https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


https://www.hackerrank.com/challenges/np-sum-and-prod/problem
import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))

https://www.hackerrank.com/challenges/np-min-and-max/problem
import numpy as np

n,m = map(int,input().split())
print(np.array([input().split() for _ in range(int(n)) ] ,int).min(1).max())


https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], dtype=int)
b = numpy.array([input().split() for _ in range(n)], dtype=int)

print(numpy.dot(a,b))

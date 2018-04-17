import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
        
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s);
	
	
	
	
	
	
	""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    if root is None:
        return True
    stack=[(float('-inf'),root,float('+inf'))]
    while stack:
        mind,node,maxd=stack.pop()
        if not(mind<node.data<maxd):
            return False
        if node.left is not None:
            stack.append((mind,node.left,node.data))
        if node.right is not None:
            stack.append((node.data,node.right,maxd))
    return True        

	https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
	
	n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

while True:
    SwapsFlag = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps += 1
            SwapsFlag = True
    if not SwapsFlag:
        break


print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])




def has_cycle(head):
    count=0
    while head.next:
        head=head.next
        count+=1
        if count>100:
            return True
    return False
	
	
	https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
	
	s = int(input().strip())

seen={0:1}
def combine(n):
    if n<0:
        return 0
    if n in seen:
        return seen[n]
    ret= combine(n-1)
    ret+=combine(n-2)
    ret+=combine(n-3)
    seen[n]=ret
    return ret
for a0 in range(s):
    n = int(input().strip())
    print(combine(n))

	
	https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
	
	#!/bin/python3

import sys
from functools import reduce
from operator import xor


def lonely_integer(a):
    return reduce(xor,a)
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))




https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def number_needed(a, b):
    count=0
    for i in range(97,123):
        ia=a.count(chr(i))
        ib=b.count(chr(i))
        count+=abs(ia-ib)
    return count    
#    pass

a = input().strip()
b = input().strip()

print(number_needed(a, b))

https://www.hackerrank.com/challenges/ctci-ransom-note/problem

from collections import Counter
def ransom_note(magazine, ransom):
    return (Counter(ransom)-Counter(magazine)) =={}

    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    


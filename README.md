# hackerrank-python

[make-it-anagram-mglines](https://www.hackerrank.com/challenges/make-it-anagram-mglines/problem)
```
w1 = raw_input()
w2 = raw_input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    total += abs(w1.count(letter) - w2.count(letter))
print total
```

[python-time-delta](https://www.hackerrank.com/challenges/python-time-delta/problem)
```
#!/bin/python3

import sys
from datetime import datetime
from dateutil.parser import parse
fmt = "%a %d %b %Y %H:%M:%S %z"

def time_delta(t1, t2):
    
    fmt = "%a %d %b %Y %H:%M:%S %z"
    ts1 = datetime.strptime(t1, fmt)
    ts2 = datetime.strptime(t2, fmt)
    if ts1 > ts2:
        td = ts1 - ts2
    else:
        td = ts2 - ts1
    return int(td.total_seconds())
    

    for i in range(int(input())):
        t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        print(abs(int((t1-t2).total_seconds())))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
```
		
[any-or-all](https://www.hackerrank.com/challenges/any-or-all/problem)
```
_,a=raw_input(),raw_input().split()
print all(map(lambda x: int(x)>0,a)) and any(map(lambda x: all(map(lambda y: x[y]==x[-y-1], xrange(len(x)/2))),a))		
```
[py-collections-deque](https://www.hackerrank.com/challenges/py-collections-deque/problem)
```
from collections import deque
d=deque()
for _ in range (int(input())):
    inp=input().split()
    getattr(d,inp[0])(*[inp[1]] if len (inp)> 1 else[])
print(*[item for item in d])    
```
[piling-up](https://www.hackerrank.com/challenges/piling-up/problem)
```
# Enter your code here. Read input from STDIN. Print output to STDOUT
for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print "Yes" if i == l - 1 else "No"
	
```
[most-commons](https://www.hackerrank.com/challenges/most-commons/problem)
```	
#!/bin/python3

import sys
from collections import Counter, OrderedDict
if __name__ == "__main__":
    s = input().strip()
    c = Counter(s).most_common()
    #print(type(c))
    for element in sorted(c, key=lambda x: (-x[1], x[0]))[:3]:
        print(" ".join(str(e) for e in element), sep=" ")
		
		
```

[python-sort-sort](https://www.hackerrank.com/challenges/python-sort-sort/problem)
```	
#!/bin/python3

import sys

from operator import itemgetter
N, M = map(int, input().split())

lst = [[int(i) for i in input().split()] for _ in range(N)]

for i in sorted(lst, key=itemgetter(int(input()))):
    print(*i)
	
```	
[set-union](https://www.hackerrank.com/challenges/py-set-union/problem)
	```
	print(input() == 0 or len(set(input().split()).union(input() == 0 or input().split())))
```

[intersection-operation](https://www.hackerrank.com/challenges/py-set-intersection-operation/problem)
```	
	print(input()==0 or len(set(input().split())&(input()==0 or set(input().split()))))
```

	
[set-difference-operation](https://www.hackerrank.com/challenges/py-set-difference-operation/problem)
```	
	_,a,_,b=[set(input().split()) for _ in '1234'];print(len(a-b))

```

[set-symmetric-difference-operation](https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem)
```	
a=int(input())
a1=input()
b=int(input())
b1=input()
k1=a1.split(" ")
k2=b1.split(" ")
k1n= list(map(int, k1))
k2n= list(map(int, k2))
ms1=set(k1n)
ms2=set(k2n)
l=ms1.symmetric_difference(ms2)
print(len(l))

```

[matrix-script](https://www.hackerrank.com/challenges/matrix-script/problem)
```
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
```

[validating-postalcode](https://www.hackerrank.com/challenges/validating-postalcode/problem)
```
import re

print(bool(re.match(
    r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$', input()
)))
```

[python-tuples](https://www.hackerrank.com/challenges/python-tuples/problem)
```
if __name__ == '__main__':
    n = int(input())
    input_line = raw_input()
    input_list = input_line.split()
    for i in xrange(n):
        input_list[i] = int(input_list[i])
    t = tuple(input_list)
    print hash(t)
```
    
[list-comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem)
```
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])

```

[find-second-maximum-number-in-a-list](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)
```	
i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)

```

[nested-list](https://www.hackerrank.com/challenges/nested-list/problem)
```
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
```

[finding-the-percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem)
```
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
```

[designer-door-mat](https://www.hackerrank.com/challenges/designer-door-mat/problem)
```	
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
```

[merge-the-tools](https://www.hackerrank.com/challenges/merge-the-tools/problem)
```
def merge_the_tools(S,N):
    for part in zip(*[iter(S)] * N):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
    
```
	
[the-minion-game](https://www.hackerrank.com/challenges/the-minion-game/problem)
```	
    def minion_game(s):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"
    
```	

	
[map-and-lambda-expression](https://www.hackerrank.com/challenges/map-and-lambda-expression/problem)

```
	cube = lambda x: pow(x,3)
def fibonacci(n):
    
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])
	```
	
[validate-list-of-email-address-with-filter](https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem)
```	
	def fun(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True

    # return True if s is a valid email, else return False
```

	
[reduce-function](https://www.hackerrank.com/challenges/reduce-function/problem)
```	
	import operator
	from fractions import Fraction
from functools import reduce
def product(fracs):
    t =  reduce(operator.mul , fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator
	
	if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
```

[capitalize](https://www.hackerrank.com/challenges/capitalize/problem)
```
def capitalize(s):
    for x in s[:].split():
        
        s = s.replace(x, x.capitalize())

    return s
	
	if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
```

[find-a-string](https://www.hackerrank.com/challenges/find-a-string/problem)
	```
	if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
	
	def count_substring(string, substring):
    counter=0
    i=0
    while i<len(string):
        if string.find(sub_string,i)>=0:
            i=string.find(sub_string,i)+1
            counter+=1
        else: break
    return counter
```
```
	
[text-wrap](https://www.hackerrank.com/challenges/text-wrap/problem)
```	
	if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
	
	def wrap(s,w):
    l = " ".join(textwrap.wrap(s,w))
    return textwrap.fill(l,w)
```     

	 
[python-string-formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem)
```
if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
	def print_formatted(n):
    width = len("{0:b}".format(n))
    for i in xrange(1,n+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)
	``` 
	 

#!/bin/python3

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    arr=[]
    l=int(len(rating))
    for i  in range(len(rating)):
        if (rating[i]>89):
            arr.append(rating[i])
            
    c=0
    a=len(arr)
    for j in range(a):
        c+=arr[j]
    d=c/a    
    d=round(d,2)
    d=format(d, '.2f')
    print(d) 

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)

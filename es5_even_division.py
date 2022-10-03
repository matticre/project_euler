'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder. What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

#work in progress!!!

from math import *

def prime(n):
    prime=[]
    for i in range(2,n+1):
        test=True
        for j in range (2, int(sqrt(i))+1):
            if i%j==0:
                test= False
            
        if test:
            prime.append(i)
    print(prime)

prime(20)



def number():
    prime=[2**4,9,5,7,11,13,17,19]
    prod=1
    for i in prime:
        prod = prod * i
    print(prod)

number()

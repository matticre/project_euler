from math import *

def prime (n):
    max = 0
    while (n>1):
        for i in range(2,int(sqrt(n))):
            if n%i==0:
                n = n/i
                if i>max:
                    max = i
                continue

    print ("The biggest prime number is: ", max)

prime(600851475143)
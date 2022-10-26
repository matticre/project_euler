
'''
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

#this function checks if the number is a palindrome
def palindrome(n):
    if n%11!=0:
        return False
    else:
        n = str(n)
        n_reverse = n[::-1]
        if n==n_reverse:
            return True
        else:
            return False

#now, I make all the possible products between three digit numbers
max=0

for i in range(0,999):
    for j in range(0,999):
        if palindrome(i*j):
            if i*j>max:
                max=i*j

print(max)
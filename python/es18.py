import os
import numpy as np

list = np.array([])

f=open("es18.txt",'r')
for x in f:
    print(x)
    s=f.readline()
    s=s.split()
    for j in range(len(s)):
        s[j] = int(s[j])
    list = np.append(list, s)

print (list)
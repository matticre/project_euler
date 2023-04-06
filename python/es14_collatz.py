def collatz (n):
    if (n%2==0):
        return n/2
    else:
        return 3*n+1

list = []
max = 0

for n in range (1,1000000,2):
    counter = 0
    number = n

    while(number!=1):
        number = collatz(number)
        counter += 1

    if counter>max:
        max = counter
        max_number = n

print(max_number, " ", max)
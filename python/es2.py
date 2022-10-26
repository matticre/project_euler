def fibonacci(n):
    sum=1
    tot=0
    previous=1

    while(sum<n):
        if sum%2==0:
            tot = tot + sum
        temporary = sum
        sum = sum + previous 
        previous = temporary

    print ("La somma è ", tot)

fibonacci(4000000)
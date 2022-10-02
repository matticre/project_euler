def sum(num):
    tot=0

    for n in range(1,num):
        if n%3==0:
            tot = tot + n
        elif n%5==0: 
            tot = tot + n
    print ("La somma è ", tot)

sum(1000)
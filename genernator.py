# solution 1

for i in range(1,5):
    print(i)



#solution 2

def prime(start,end):
 
    for num in range(start,end + 1):  
     if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
               break  
            else:
                yield num

g=prime(2,20)
print(next(g))


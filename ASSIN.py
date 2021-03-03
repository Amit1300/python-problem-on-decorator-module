def add_up(n):
    sum=0
    if(type(n)==int):
        for i in range(n+1):
            sum+=i
        print(sum)
    else:
        print("number is not integer")
print(add_up(9))



def check(list1):
    for i in list1:
        if(i%4==0):
            if(i>120):
                break
            else:
                print(i)
list1=[8,15,32,42,60,75,122,150,180,190]
check(list1)


def rev(list2):
    list3=[]
    for i in range(len(list2)-1,0,-1):
        print(list2[i])
        list3.append(list2[i])
    print(list3)
    
num1=[5,15,20,25,30]    
rev(num1)
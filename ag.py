def give_firstletter(string):
        return string[0]
print(give_firstletter("Hello World"))
    
# question 2

x="tinker"
print(x[1:4])




#question 3

def unique_letter(string2):
    return  set(list(string2))

print(unique_letter('Mississippi'))

#question 4

def change_tuple(x):
    new_tuple=[(i[0],i[1])+(100,) for i in x]
    return new_tuple

    
print(change_tuple([(10, 20, 30), (40, 50, 90), (70, 80, 60)]))



def combination(x):
    list1 = x.get('1')
    print(list1)
    list2 = x.get('2')
    for i in range(2):
     for j in range(2):          
        print(list1[i]+list2[j])



obj ={'1':['a','b'], '2':['c','d']}

print(combination(obj))


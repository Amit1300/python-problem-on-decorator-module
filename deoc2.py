def standard_phone_no(func):
    def wrapper(n):
        l=func(n)
        new_list=[]
        final_list=[]
        for i in l:
            if (i[0:2]=="+91"):
                standard_no=i
            else:
                standard_no="+91"+i[2:]
            
            
            new_list.append(standard_no)

        sorted_phone=(sorted(new_list,key=lambda x:x[2:5]))
        for i in sorted_phone:
            final_list.append((int(i)))
            print(int(i))
        return final_list
    return wrapper


@standard_phone_no
def take_phone_no(n):
  phone_list=[]
  for i in range(n+1):
    phone_no=input("enter phone no")
    if len(phone_no)==12:
      phone_list.append(phone_no)
    else:
      print("write appropiate phone number")

  return phone_list

print(take_phone_no(1))
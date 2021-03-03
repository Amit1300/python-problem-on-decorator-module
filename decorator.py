
def do_sort(func):
  def wrapper(n):
    d=func(n)
    sor=sorted(d,key=lambda x:x["age"])
    for i in sor:
      print(i["first_name"])
    return sor
  return wrapper


  
  

@do_sort
def data(n):
  l=[]
  for i in range(n+1):
    data=dict()
    data["first_name"]=input("enter your first name")
    data["last_name"]=input("enter your first last")
    data["age"]=int(input("enter your age"))
    data["sex"]=input("enter your first gender")
    l.append(data)
  return l


print(data(1))


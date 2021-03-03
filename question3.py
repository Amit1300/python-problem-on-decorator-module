def read():
    with open("amit.txt","r") as f:
        r=f.read()
        f.close()
    yield r

        
    
v=read()
print(type(v))
print(next(v))





def fn1():
    name=input("Enter your name:")
    return name

def fn2():
    age=input("Enter your age:")
    age=int(age)
    return age

def fn3():
    career=input("Enter your path:")
    return career
    
name=fn1()
age=fn2()
career=fn3()

print("---THIS CANDIDATE'S DETAILS ARE---")
print("Name: "+name+"\nAge:"+str(age)+"\nCareer:"+career)
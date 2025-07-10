age = int(input("what is your age?: "))

if (age >= 18):
    print("your are an adult")
    
if (age>=1 and age <13):
    print("you are a child")
    
elif (age>=13 and age <20):
    print("you are a teenager ") 
    
elif (age >=20 and age <50):
    print("you are a old person")          
elif (age == 18):
    print("your are an adult")
    
else:
    print("your are not an adult")        
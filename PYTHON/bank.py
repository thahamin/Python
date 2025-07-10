number = input("write your phoen number: ")

if len(number) >11:
    print("your number is too long")
    
elif len(number) < 11:
    print("your number is too short") 
    
elif len(number) == 11:
    print("thank you,",number)
           
else:
    print("ypur number is not valid")           
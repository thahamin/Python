number = 10

if number%3 ==0:
    if number%5 ==0:
        print(number,"fizzbuzz")
    else:
        print(number,"fizz")
            
    
elif number%5 ==0:
    print(number,"buzz")
    
elif number%3 ==0 and number%5 ==0:
    print(number,"Number is fizzbuzz")    
    
print("finished")    
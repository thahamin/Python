check = ""
light_on = False
while check != 'sleep':

    check = input("< ").lower()
    if check == 'on':
        if light_on:
            print("light is aleready in on mode")
        else:
            light_on = True
            print("lisht turned on mode")

    elif check == 'off':
        if not light_on:
            print("light is already in off mode")
        else:
            light_on = False
            print("light turned off mode")

    elif check == 'sleep':
        break

    elif check == 'help':
        print('''1. on - light on
2. off - light off
3. sleep - exit program''')

    else:
        print("i don't understand your command.")
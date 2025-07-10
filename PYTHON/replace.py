first_Name = input("write your first name: ")
second_Name = input("write you seconf name: ")

Full_Name = f"{first_Name} {second_Name}"
print('your full name is:',Full_Name)
print("Title formate:", Full_Name.title())
print("Upper case formate:", Full_Name.upper())

change_second_name = input('replace your scind name: ')

new_full_name = Full_Name.replace(second_Name, change_second_name)

print(Full_Name,"your new full name is",  new_full_name)

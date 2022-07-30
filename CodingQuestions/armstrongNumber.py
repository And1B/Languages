num = input("Input a number here: ")
helper = 0

for number in num:
    helper += int(number)**3
    
if(helper == int(num)):
    print("Success")
else:
    print("Not an Armstrong Number")

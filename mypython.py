#Identifying number of digits#
num=input("Enter a Number")
if 9 < num < 99:
    print("This is a Two Digit Number")
elif 99 < num < 999:
    print ("This is a Three Digit Number")
elif 999 < num < 9999:
    print ("This is a Four Digit Number")
else:
    print("Number is <= 9 or >= 9999")





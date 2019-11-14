#Odd can't be divided by 2
#Even can be divided by 2

number = float(input("Say a number and I will tell you if it is even or odd."))
answer = number % 2

if answer > 0:
    print("Odd")

else:
    print("Even")

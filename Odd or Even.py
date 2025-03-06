#check if a number is odd or even dividing it by 2

number1 = input("what is the number you want to know if it's even or odd?: ")
number1 = int((number1))

if number1 % 2 == 0:
    print("It is even")
else:
    print("it is uneven")

first = input("please enter a number : ")
operator = input("please enter desired operation(+,-,*,/) : " )
second = input("please enter second number : ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
else :
    print("invalid input, please check input above")


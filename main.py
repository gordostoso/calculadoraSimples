
operetor = input("enter one operetor: + - * / ")
num_1 = float(input("enter the 1st number"))
num_2 = float(input("enter the 2nd number"))

if operetor == "+":
    print(num_1+ num_2)
elif operetor == "-":
    print(num_1 - num_2)
elif operetor == "*":
    print(num_1 * num_2)
elif operetor == "/":
    print(num_1 / num_2)
else:
    print("invalid operetor")
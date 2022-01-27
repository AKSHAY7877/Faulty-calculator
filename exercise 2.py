#                       Faulty Calculator By Akshay Sharma
print("Enter the two numbers")
a = float(input())
b = float(input())
print("Specify your operation: '+' '-' '*' '/' '%' '**'")
o = input()
if a == 45 and b == 3 and o == "*":
    result = 555
elif a == 56 and b == 9 and o == "+":
    result = 77
elif a == 56 and b == 6 and o == "/":
    result = 4
elif o == "*":
    result = a*b
elif o == "/":
    result = a / b
elif o == "+":
    result = a + b
elif o == "-":
    result = a - b
elif o == "%":
    result = a % b
elif o == "**":
    result = a ** b
else:
    print("ERROR :: Specify correct operation")
    exit(1)
print("Result is : ",result)
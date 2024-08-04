print("1. Sum")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")

op= int(input("\nEnter the operation from the above list: "))
a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))

match op:
    case 1: print("\nSum is",a+b)
    case 2: print("\nSubstraction is",a-b)
    case 3: print("\nMultiplication is",a*b)
    case 4: print("\nDivision is",a/b)
    case 5: print("\nReminder is",a%b)
    case _: print("\nSomething went wrong")
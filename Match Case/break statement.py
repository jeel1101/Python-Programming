n= int(input("Enter the number: "))

print("\n")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    if(i==10):
        break
    
print("\nLoop is over")
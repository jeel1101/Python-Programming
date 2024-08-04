try:
    n= int(input("Enter the number: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
except ValueError:
    print("Invalid Syntax!")
    
print("Some important short code")
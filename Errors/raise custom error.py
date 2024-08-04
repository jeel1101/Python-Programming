a= int(input("Enter the number between 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("\nValue should be between 5 and 9")
    
else:
    print(f"\nNumber is {a}")
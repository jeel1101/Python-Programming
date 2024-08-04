try:
    l={1,5,6,7}
    i=int(input("Enter the index: "))
    print(l[i])

except:
    print("\nSome error occured")
    
finally:
    print("\nI am always executed")
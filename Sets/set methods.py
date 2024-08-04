s1= {1,2,3,4,5,6}
s2= {7,6,8,9}
cities= {"Anand","Mumbai","Delhi","Rajkot","Ayodhya"}
cities2= {"Delhi","Vadodara","Anand","Mahomet"}

print(s1.union(s2))
s1.update(s2)
print(s1,s2)            # union() and update() method

cities3= cities.intersection(cities2)
cities4= cities.intersection_update(cities2)
print(cities3)
print(cities)               #intersection() method and intersection_update() method

print(cities.isdisjoint(cities2))   # isdisjoint() method

print(cities.issuperset(cities2))

print(cities.issubset(cities2))

cities.add("Goa")
print(cities)

cities.update(cities2)
print(cities)

cities.remove("Delhi")
print(cities)

cities3= cities.pop()
print(cities3)
print(cities)

# del cities
# print(cities) # Error

cities.clear()
print(cities)
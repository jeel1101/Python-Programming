nums= [19,5,20,45,8,56,15,19,5]
colors= ["Blue","Orange","Yellow","Green","Pink"]

nums.sort()
print(nums)         # list.sort() method

nums.append(99)
print(nums)         # list.append() method

nums.reverse()
print(nums)         #list.reverse() method

print(nums.index(20))        #list.index() method

print(nums.count(19))        #list.count() method

newList= nums.copy()
print(newList)               #list.copy() method

nums.insert(5,100)
print(nums)                  #list.insert() method

nums.extend(colors)
print(nums)                  #list.extend() method

print(nums + colors)         #concatenation of lists
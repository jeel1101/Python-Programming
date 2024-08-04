info= {'name':'Jeel', 'age':20, 'eligible':True}

info.update({'age':22})
info.update({'DOB': '11-01-2005'})
print(info)     # update() method

# info.clear()
# print(info)     # clear dictionary

# info.pop('age')
# print(info)         # remove entered parameter

info.popitem()
print(info)       # remove last key and value

# del info
# print(info)       # delete dictionary


# set -> Store non-duplicate items
#     -> very fast than list
#     -> useful for large data
#     -> 

# create set
x = {2,4,3,2,5,6,5,3}
y = {2,3,5,1,7,9,7,4,3,5}
print("x :",x)

# add
x.add(12)
print("x :",  x)

# add
x.remove(2)
print("x :",  x)

# pop for removing random item
x.pop()
print("x pop:",  x)

# delete all item
x.clear()
print("x :",  x)

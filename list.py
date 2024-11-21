# Data structure List
data1 = [1, "nama", True]
data2 = [0,1,2,3,4,5,6,7,9]
tuple1 = (1,2,3,4)
print(type(list(tuple1)))

# List comprehension
a = [a for a in data1]
print(a)
b = [b**2 for b in data2]
print(b)
c = [c**2 for c in data2 if c % 2 == 0 ]
print(c)

# delete
x = [2,4,6,8]
del(x[2])
print(x)

# append
x.append(10)
print(x)

# extend
x.extend([12,14])
print(x)

# insert
x.insert(1,[1,3])
print(x)

# pop -> return item
print(x.pop())
print(x)

# remove -> menghilangkan element pertama dari nilai tertentu
x.remove(4)
print(x)

#reverse 
x.reverse()
print(x)

# reverse sort
y = [5,3,6,2,7,4,6,4,2]
y.sort(reverse=True)
print(y)

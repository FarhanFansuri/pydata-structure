# Indexing -> accesing data element
# Index starts with 0

x = "frog"
print(x[3]) 

# slicing
num = [0,1,2,3,4,5,6,7,8,9]
y = "computer"
print(y[:-2])
print(num[1:6:2])
print(num[::-1])
print(num[1:6][::-1])

# concatination
word = "yaya " + "cika"
print(word)

list_num = [1,2,3] + [4,5]
print(list_num)

tuple_num = (1,2,3) + (4,5)
print(tuple_num)

# multiplaying
word3 = "word " * 3
print(word3)

tuple3 = (1,2) * 3
print(tuple3)

list3 = [1,3] * 3
print(list3)

# checking membership
b = "bug"
print('b' in b)

c = "carrot"
print('car' in c)

c = ["carrot", "banana", "apple"]
print('carrot' not in c)

# enumeration
for i,v in enumerate(c):
    print("index",i,":", v)

# number of items
print(len(num))

# min & max
print(min(num))
print(max(num))
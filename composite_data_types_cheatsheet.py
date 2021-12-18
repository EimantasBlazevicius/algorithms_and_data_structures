# Lists
listas = []
listas2 = [1,2,3,4,56,7,8,9]

listas.append(5)
listas.append(5)
listas.append(5)
listas.append(4)
listas.append(3)

length = len(listas)
index_of_three = listas.index(3)
amount_of_fives_in_the_list = listas.count(5)
listas.extend(listas2)  # Lists extension
listas.insert(1, 99)  # at the index insert value
last = listas.pop()  # remove and return last element
listas.remove(5)  # remove first occurance of item
listas.sort()
listas.reverse()
# print(listas)

# Dictionaries
dict1 = {'color': "red", 'bottle': 'full'}
dict2 = {'number': 42, 'shape': 'circle'}

dict1.update(dict2)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print(dict1.get('bottle'))  # get value by the key
print(dict1.pop('shape'))  # delete key, value pair value by the key

# Tuples
numbers = 1,2,[1,2,34,5],45,6,9,7,5,96,9,4,4,4,
numbers2 = (1,2,3)
numbers3 = tuple(listas)
print(numbers.count(6))
print(numbers.index(6))
numbers[2][1]= 9999
len(numbers)

# Set
setas = set(listas)
# setas.clear()
setas2 = setas.copy()
setas.add(9)
setas.discard(9)
setas.union(setas2)
setas.update([9,5,1,67,8,8,8,8,8,6,7,1,32,6,5,4,9,7,98,45,4,54,54,54,54,54])
print(setas.difference(setas2))
print(setas)



x = {"apple", "banana", "cherry","google"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("z:",z)
#Compare 3 sets, and return a set with items that is present in all 3 sets
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

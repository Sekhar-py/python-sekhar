#Return True if all items set y are present in set x
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print("z:",z)

#Return False if not all items in set y are present in set x
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

m = x.issuperset(y)

print("m:",m)

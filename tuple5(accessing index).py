#You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#negitive index
thistuple = ("apple", "banana", "cherry")
print("negitive index:",thistuple[-1])
#range of index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("range:",thistuple[2:5])

#By leaving out the end value, the range will go on to the end of the list:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("First to end value:",thistuple[:4])

#stat index to end value of index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("start to end:",thistuple[2:])

#This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

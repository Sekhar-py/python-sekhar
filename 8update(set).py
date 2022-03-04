thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Add elements of a list to at set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#Add elements a tuple to at set
s={"a","b","c"}
t=(1,2,30)
s.update(t)
print(s)
#Add elements a Dict to at set
d={"s","c"}
e={1:"sekhar",2:"ram"}
d.update(e)
print(d)

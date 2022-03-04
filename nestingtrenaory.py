a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
min=a if a<b<c else b if b<c else c
print(min)
# Use the format() method to insert numbers into strings
age = 30
txt = "My name is sekhar, and I am {}" # {} fill the number by using format operator
print(txt.format(age))

quantity = 4
itemno = 500
price = 450
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 4 #zero postion
itemno = 500 #1st postion
price = 450 #2nd postion
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print("the intger is:{}".format(123))
print("the integer is :{:08d}".format(123)) # zeros precid with zero
print("the float is {:10.3f}".format(123.451234)) # 10 spaces prefix and 3 spaces postfix
print("binary:{0:b}".format(10)) #zero and binary
print("octal:{0:o}".format(10)) #zero and octal
print("hexdecimal:{0:x}".format(10)) # zero and hex
print("{:7d}".format(123))#7 means spaces
print("{:<10d}".format(190)) #left alignment
print("{:>10d}".format(2000)) #Right alignment
print("{:^10d}".format(1900)) #center alignment using ^ symbol


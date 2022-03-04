#Make the first letter in each word upper case:

txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "grand opening my 2nd python"
y= txt.title()
print(y)

#Note that the first letter after a non-alphabet letter is converted into a upper case letter:

txt = "hello b2b2b2 and 3g3g3g"

z = txt.title()

print(z)
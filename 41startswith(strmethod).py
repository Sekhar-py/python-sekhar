#Check if the string starts with "Hello":

txt = "Hello, welcome to my world."
x = txt.startswith("Hi")
print(x)

#Check if position 7 to 20 starts with the characters "wel":

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)
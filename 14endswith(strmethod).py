txt = "Hello, welcome to my world."
x = txt.endswith(".") # if it ends with . it returns True of result.
print("x:",x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.") # my world string  is endswith word it returns results True.
print("x1:",x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11) # the string in between 5 to 11  characters result is True other wise False
print("x2",x)

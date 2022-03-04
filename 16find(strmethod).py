txt = "Hello, welcome to my world."
x = txt.find("welcome") # it find character postion
print("welcome:",x)

txt = "Hello welcome to my world."
x = txt.find("e")
print("e value:",x)

txt = "Hello,welcome to my world."
x = txt.find("e", 5, 10)
print("x pos 5 to 10:",x)

txt = "Hello, welcome to my world."
print(txt.find("q")) # it is not found then return output -1
print(txt.index("q")) # not found raise exception


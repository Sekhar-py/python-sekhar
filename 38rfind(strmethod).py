txt = "hello python human."
x = txt.rfind("python")
print("x:",x)

txt = "Hello welcome to python."
x = txt.rfind("python")
print("x1:",x)
#Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hellowelcometomyworld"
y = txt.rfind("e", 5, 10)
print("y:",y)

txt = "Hello, welcome to my world." #f the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
print(txt.rfind("q"))
print(txt.rindex("q"))
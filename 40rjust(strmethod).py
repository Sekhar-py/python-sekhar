#Return a 50 characters long, right justified version of the word "banana":

txt = "banana"
x = txt.rjust(30)
print(x, "is my favorite fruit.")

#Using the letter "#" as the padding character:

txt = "banana"
x = txt.rjust(20, "#")
print(x)

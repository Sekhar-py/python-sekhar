txt = "                banana               "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

txt = "banana,,,,,###ssqqqwwzz.....@"

x = txt.rstrip(",.#qswz@")

print(x) #Remove the trailing characters if they are commas, s, q, or w:
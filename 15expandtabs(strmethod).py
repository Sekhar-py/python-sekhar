txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs()) # string.expandtabs(tabsize) defult tab size is 8.
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


g="sekhar \t is \t great"
print(g.expandtabs(30))
txt = "I like bananas" #Replace the word "bananas":
x = txt.replace("bananas", "apples")
print(x)
#Replace all occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "suny leon")
print(x)

#Replace the two first occurrence of the word "one"
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

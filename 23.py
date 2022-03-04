t=('100','30','40')
if '10'in t:
    y=list(t)
    y.append("12+13j")
    print(y)
else:
    y=list(t)
    y.remove('30')
    print(y)
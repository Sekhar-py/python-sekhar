t=('10','12.45',13+4j)
y=list(t)
y[0]="dad"
y[1]="True"
y[2]="False"
t=tuple(y)
print(t)
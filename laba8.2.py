n=int(input("Введите порядок массива"))
a=[]
for i in range(n):
    a.append([float(x) for x in input("Введите массив(каждую строку с новой строки,числа через пробел)").split()])
m=0
x=0
y=0
for i in range(n):
    for q in range(n):
        if abs(a[i][q])>m:
            m=abs(a[i][q])
            x=i
            y=q
a[0],a[x]=a[x],a[0]
for i in range(n):
    a[i][0],a[i][y]=a[i][y],a[i][0]
for r in a:
    print(r)

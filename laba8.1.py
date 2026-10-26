n=input("Введите количество чисел")

print("Введите числа через пробел")
a=[float(x) for x in input().split()]

print("Введите границы отрезка(левую и правую)")
x,y=map(float, input().split())

if x>y:
    x,y=y,x

r=1
f=False
for v in a:
    if x<=v<=y:
        r*=v
        f=True
if f:
    print(r)
else:
    print("В отрезок не попало ни одного числа")


a,b,c = map(int, input().split())
if (a==0) or (b==0) or (c==0):
    print('это не квадратное уравнение')
elif a+b+c==0:
    x1=1
    x2=c/a
    print(x1, x2)
elif a-b+c==0:
    x1=-1
    x2=-1*c/a
    print(x1, x2)
else:
    d=b**2-4*a*c
    if d<0:
        print('данное уравнение не имеет действительных решений')
    else:
        x1=(-1*b-d**0.5)/2*a
        x2=(-1*b+d**0.5)/2*a
        print(x1,x2)
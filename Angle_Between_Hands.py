n=input().split(':')
n=list(n)
h=int(n[0])
mi=int(n[-1])
an=abs((30*h)-((11/2)*mi))
if an<180:
    print(an)
else:
    print(360-an)
a,b=map(int,input().split())
c=a+1
d=a-1
if(c==b or d==b):
    print('Yes')
elif(a==1 and b==10 or(a==10 and b==1)):
    print("Yes")
else:
    print('No')
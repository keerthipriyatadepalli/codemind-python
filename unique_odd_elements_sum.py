n=int(input())
l=list(map(int,input().split()))
b=set(l)
sum=0
for i in b:
    if(i%2!=0):
        sum+=i
print(sum)
        
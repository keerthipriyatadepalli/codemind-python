n=int(input())
l=list(map(int,input().split()))
b=set(l)
sum=0
for i in b:
    sum+=i
print(sum)
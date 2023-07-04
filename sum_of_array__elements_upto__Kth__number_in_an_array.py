n=int(input())
l=list(map(int,input().split()))
k=int(input())
sum=0
for i in l:
    if(k>=i):
        sum+=i
print(sum)
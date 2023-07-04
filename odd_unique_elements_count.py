n=int(input())
l=list(map(int,input().split()))
b=set(l)
count=0
for i in b:
    if(i%2!=0):
        count+=1
print(count)

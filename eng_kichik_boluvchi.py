n=int(input())
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print(a[0])

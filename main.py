e=int(input())
n=int(input())
arr=[]
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
    arr.sort()
    ans=0
for i in range(n-1,-1,-1):
    mini=0
    while(e>0 and mini<2):
        e=e-arr[i]
        mini+=1
        ans+=1
if e<=0:
    print(ans)
else:
    print("-1")

e=int(input())
n=int(input())
a=[]
for i in range(0, n):
   ele = int(input())
   a.append(ele)
a.sort()
c=0
for i in range(n-1,-1,-1):
   mini=0
   while(e>0 and mini<2):
       e=e-a[i]
       mini+=1
       c+=1
if(e<=0):
   print(c)

else:

   print(-1)


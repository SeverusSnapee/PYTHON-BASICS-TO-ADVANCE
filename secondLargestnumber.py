n=int(input())
l=[]
c=0
    

l= list(map(int,input().split())) 
    # b=int(input())
    # l.append(b)
    
l.sort()
for i in range(int(n)):
    if(l[i]==l[n-1]):
        c=c+1
print(l[n-c-1])
 
                
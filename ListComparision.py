a=int(input())
b=int(input())
c=int(input())
n=int(input())
lst=[]
for i in range(0,int(a)+1):
    for j in range(0,int (b)+1):
        for k in range(0,int (c)+1):
            if(i+j+k!=n):lst.append([i,j,k])             
print (lst)
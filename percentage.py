n=int(input())
l=[]
m=[]
for i in range(int(n)):
    l.append(input())
    m.append([int(input()),int(input()),int(input())])
x=input()
for  i in range(int(n)):
    if(l[i]==x):
        u=float(float(m[i][0])+float(m[i][1])+float(m[i][2]))
        v=float(u/3)
print(v)

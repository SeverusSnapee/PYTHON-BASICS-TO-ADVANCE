n=int(input())
name=[]
score=[]
y=[]
b=[]
x=2
    # for i in range(int(n)):
for i in range(int(n)):
         j=input()
         name.append(j)
         l=float(input())
         score.append(l)
  
lowest=score[0]    
  
for j in range(int(n)):
  if(score[j]<=lowest):
    lowest=score[j] 
    x=j;
print(score[x])
score.remove(score[x])
name.remove(name[x])
lowest=score[0]  
for o in range(int(n)-1):
    if(score[o]<=lowest):
         lowest=score[o] 
         u=o;
# for j in range(int(n)):
#   if(score[j]==score[x]):
#      b.append(j)
# u=len(b)
# for j in range(len(b)):
#      score.remove(score[b[j]])
#      name.remove(name[b[j]])
# lowest=score[x]
# for i in range(int(n)-u):
#     if(score[i]<=lowest):
#      lowest=score[i]
  
# for i in range(int(n)-1):
#     if(score[i]==lowest):
#         y.append(name[i])
# y.sort()

# for i in range(len(y)):
#     print(y[i])
print (score[u])
nterms = int(input("Enter the no of terms "))
n1 , n2 = 0 , 1
count = 0
if nterms==1 : print("Series",n1)
elif nterms>0 : 
    print("Fibbanco Series ")
while count<nterms :
    n3=n2+n1
    print(n3)
    n1=n2
    n2=n3
    count+=1
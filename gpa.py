n,m=input().split()
letter_grades=input().split() #
weights=input().split() #
a={}
t=int(m)
for i in range(t):
    Credits,point = input("Credits :").split()
    a.update({Credits:point})
x=w=n=0

for j in letter_grades :
    v=float(a.get(j))
    l=weights[n]
    x=x+v*int(l)
    w=w+int(l)
    n=n+1
GPA=round(x/w,2)

p=a.get(j)
min_ = abs(float(p)-GPA)

for i in  a.values():
    t=abs(float(i)-GPA)
    if t < min_ :
        min_ = t
        p=str(i)

L1=list(a.values())
x=L1.index(p)
L2=list(a.keys())
y=L2[x]
#print(p,y)


print("Output :",GPA,"\n",y)








   
    





   
    

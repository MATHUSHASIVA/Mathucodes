P=[] #empty list

for i in range (4):
    Vectors = input().split() # input 3 direction of verctors
    P.extend([Vectors])
L=[]
n=1
for l in range (3):
    s=[]
    r=0
    for k in range (3):
        t=int(P[n][r])-int(P[0][r])
        r+=1
        s.append(t)
        print(t)
    n+=1
    L.extend([s])

n=0
x=1
vector_tripple=[]
for i in range(3):
    t=(((int(L[2][n+1])*int(L[3][n+2])) - (int(L[2][n+2])*int(L[3][n+1])))*x
    n=n-1
    vector_tripple.append(t)
    if i == 2:
        n=
    
    
    
    

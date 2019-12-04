import math
import sys
import random
eta=0.001
stp=0.001
datafile = sys.argv[1]
f=open(datafile)
data=[]
i=0
l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(a[j])
    l2.append('1')
    data.append(l2)
    l=f.readline()
rows=len(data)
cols =len(data[0])

labelfile = sys.argv[2]
f=open(labelfile)
this_class= {}
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l != ''):
    a=l.split()
    this_class[int(a[1])] = int(a[0])
    if(this_class[int(a[1])]==0):
        this_class[int(a[1])]==-1
    l=f.readline()

for k,v in this_class.items():
    if(v==0):
        this_class[k]=-1
rows=len(data)
cols=len(data[0])
w=[]
for j in range (0,cols,1):
    w.append(0)
    
for j in range (0,cols,1):
    w[j]=0.02*random.uniform(0,1)-0.01
        
int_error=0.0
for i in range(0,rows,1):
        if(this_class.get(i)!= None):
            dp=0.0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            int_error+=max(0,1-this_class[i]*dp)
print(int_error)
converged=False
count=0
while not converged:
    count+=1
    dellf=[]
    for j in range(0,cols,1):
        dellf.append(0)
    for i in range (0,rows,1):
        if(this_class.get(i)!= None):
            dp=0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            for j in range(0,cols,1):
                if(dp*this_class[i]<1):
                    dellf[j]+=-1*float(data[i][j])*this_class[i]
                else:
                    dellf[j]+=0
    for j in range(0,cols,1):
        w[j]=w[j]-eta*dellf[j]
    error=0.0
    for i in range(0,rows,1):
        if(this_class.get(i)!= None):
            dp=0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            error+=max(0,1-this_class[i]*dp)
    if abs(int_error - error) <= stp:
        converged = True 
    print(abs(int_error - error))
    int_error = error

print ("W:",w[:-1])
print ("count:",count)
normw=0
for j in range(0,cols-1,1):
    normw+=w[j]**2
normw=math.sqrt(normw)
d_origin=w[len(w)-1]/normw
print ("distance to origin:",abs(d_origin))

for i in range(0,rows,1):
    if(this_class.get(i)==None):
        dp=0
        for j in range(0,cols,1):
            dp+=w[j]*float(data[i][j])
        if(dp>0):
            print("1",i)
        else:
            print("0",i)

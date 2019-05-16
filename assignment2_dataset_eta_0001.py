import math
import sys
import random
eta=0.0001
stp=0.001
datafile = sys.argv[1]
f=open(datafile)
data=[]
i=0;
l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(a[j])
    l2.append('1')
    data.append(l2)
    l=f.readline()

#print(data)
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
    #n[int(a[0])]+=1

#print(this_class)
for k,v in this_class.items():
    #print(v)
    if(v==0):
        this_class[k]=-1
#print(this_class[10])
#eta=0.0001
rows=len(data)
cols=len(data[0])
w=[]
for j in range (0,cols,1):
    w.append(0)
    
for j in range (0,cols,1):
    w[j]=0.02*random.uniform(0,1)-0.01
    #w[j]=random.uniform(0,1)
        
int_error=0.0
for i in range(0,rows,1):
        if(this_class.get(i)!= None):
            dp=0.0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            int_error+=(-this_class[i]+dp)**2
converged=False
count=0
while not converged:
    count+=1
    #for k in range(0,1,1):  
    dellf=[]
    for j in range(0,cols,1):
        dellf.append(0)
    for i in range (0,rows,1):
        if(this_class.get(i)!= None):
            dp=0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            for j in range(0,cols,1):
                dellf[j]+=(-this_class[i]+dp)*float(data[i][j])
        #if ends here
    for j in range(0,cols,1):
        w[j]=w[j]-eta*dellf[j]
    error=0.0
    for i in range(0,rows,1):
        if(this_class.get(i)!= None):
            dp=0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            error+=(this_class[i]-dp)**2
        #if ends here
    if abs(int_error - error) <= stp:
        converged = True 
    int_error = error
    #print(cost)

print ("W:",w[:-1])
print ("count:",count)
normw=0
for j in range(0,cols-1,1):
    normw+=w[j]**2
normw=math.sqrt(normw)
#print(normw)
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




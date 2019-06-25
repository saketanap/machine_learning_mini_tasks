import math
import sys
import random
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
eta=0.001
rows=len(data)
cols=len(data[0])
w=[]
for j in range (0,cols,1):
    w.append(0)
    
for j in range (0,cols,1):
    w[j]=0.02*random.uniform(0,1)-0.01
    #w[j]=random.uniform(0,1)
#print("w1",w)        
int_error=0.0
for i in range(0,rows,1):
        if(this_class.get(i)!= None):
            dp=0.0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            int_error+=(-this_class[i]+dp)**2
converged=False
count=0
eta_list = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001,0.000000001, 0.0000000001, 0.00000000001 ]

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
#///////////////////////////////////////////
    bestobj = 1000000000000
    obj=0.0
    #count=0
    for k in range(0, len(eta_list),1):
        eta=eta_list[k]
        #count+=1
        for j in range(0,cols,1): 
            w[j]=w[j]-eta*dellf[j]
        #print("w2",w)
        error1=0.0
        for i in range(0,rows,1):
            if(this_class.get(i)!= None):
                dp=0
                for j in range(0,cols,1):
                    dp+=w[j]*float(data[i][j])
                error1+=(this_class[i]-dp)**2
        obj=error1
        if(obj<bestobj):
            bestobj=obj
            besteta=eta
        for j in range(0,cols,1):
            w[j]=w[j]+eta*dellf[j]
        #print("w3",w)
#//////////////////////////////////////////
    #print("besteta:",besteta)
    #print(count)
    eta=besteta
    for j in range(0,cols,1):
        w[j]=w[j]-eta*dellf[j]
    error=0.0
    #print("w4",w)
    for i in range(0,rows,1):
        if(this_class.get(i)!= None):
            dp=0
            for j in range(0,cols,1):
                dp+=w[j]*float(data[i][j])
            error+=(this_class[i]-dp)**2
        #if ends here
    #print(abs(int_error - error))
    if abs(int_error - error) <= 0.001:
        converged = True 
    int_error = error
    #print()

#print ("W:",w[:-1])
#print ("count:",count)
normw=0
for j in range(0,cols-1,1):
    normw+=w[j]**2
normw=math.sqrt(normw)
#print(normw)
d_origin=w[len(w)-1]/normw
#print ("distance to origin:",abs(d_origin))

for i in range(0,rows,1):
    if(this_class.get(i)==None):
        dp=0
        for j in range(0,cols,1):
            dp+=w[j]*float(data[i][j])
        if(dp>0):
            print("1",i)
        else:
            print("0",i)




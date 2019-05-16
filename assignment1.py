import math
import sys
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
    data.append(l2)
    l=f.readline()
        
rows=len(data)
cols =len(data[0])

labelfile = sys.argv[2]
f=open(labelfile)
trainlabels= {}
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l != ''):
    a=l.split()
    trainlabels[int(a[1])] = int(a[0])
    l=f.readline()
    n[int(a[0])]+=1
mean1=[]
for j in range (0, cols, 1):
    mean1.append(1)
 
mean2=[]
for j in range (0, cols, 1):
    mean2.append(1)

for i in range(0, rows, 1):
    if(trainlabels.get(i)!= None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
	        mean1[j]= float(mean1[j])+float(data[i][j])
    if(trainlabels.get(i)!= None and trainlabels[i] == 1):
        for j in range(0, cols, 1):
                mean2[j]= float(mean2[j])+float(data[i][j])

for j in range(0, cols, 1):
    mean1[j]=mean1[j]/n[0]
    mean2[j]=mean2[j]/n[1]

stde1=[]
stde2=[]
for j in range (0, cols, 1):
    stde2.append(0)
    stde1.append(0)

for i in range(0, rows, 1):
    if(trainlabels.get(i)!= None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
                stde1[j]=stde1[j]+(float(data[i][j])-float(mean1[j]))**2
    if(trainlabels.get(i)!= None and trainlabels[i] == 1):
        for j in range(0, cols, 1):
        	 stde2[j]=stde2[j]+(float(data[i][j])-float(mean2[j]))**2

for j in range(0, cols, 1):
    stde1[j]=stde1[j]/(n[0])
    stde2[j]=stde2[j]/(n[1])

for j in range(0, cols, 1):
    stde1[j]=math.sqrt(stde1[j])
    stde2[j]=math.sqrt(stde2[j])

for i in range (0, rows, 1):
    if(trainlabels.get(i)==None):
        d0=0.0 
        d1=0.0
        for j in range(0, cols,1):
	        d0=d0+((float(data[i][j])-mean1[j])/float(stde1[j]))**2
	        d1=d1+((float(data[i][j])-mean2[j])/stde2[j])**2
        if(d0<d1):
            print("0",i)
        else:
            print("1",i)


	
    	

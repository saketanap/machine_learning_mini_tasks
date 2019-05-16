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

f.close()
#print(data)
labelfile = sys.argv[2]
f=open(labelfile)
trainlabels= {}
l=f.readline()
while(l != ''):
    a=l.split()
    trainlabels[int(a[1])] = int(a[0])
    l=f.readline()
    #n[int(a[0])]+=1

#print(trainlabels)
datacols=len(data[0])
#print(datacols)
datarows=len(data)
zero_append = [0, 0]
zero_append3 = [0,0,0]
column_gini_value = []
for i in range(0, datacols, 1):
    coll=[]
    current_col=[]
    for j in range(0, datarows, 1):
        coll.append(zero_append)
    for k in range(0,datarows,1):
        coll[k][0]=float(data[k][i])
        coll[k][1]=trainlabels[int(k)]
        temp=[coll[k][0],coll[k][1]]
        current_col.append(temp)
    gini_col = []
    gini = 0.0  
    #print(current_col)
    current_col = sorted(current_col,key=lambda l:l[0])
    #print(current_col)
    for c in range(1, datarows,1):
        lsize = float(c)
        rsize = float(datarows - c)
        lp = 0
        rp = 0       
        for v in range(0,c,1):
            if(current_col[v][1] == 0):
                lp+=1  
        for v in range(c,datarows,1):
            if(current_col[v][1] == 0):
                rp+=1
        #print(lp,rp)
        gini = float(lsize / datarows) * float(lp / lsize) * float(1 -float(lp / lsize)) + float(rsize / datarows) * float(rp / rsize) * float(1- float(rp / rsize))
        sp_value=(current_col[c-1][0]+current_col[c][0])/2
        tempp=[gini,sp_value,i]
        gini_col.append(tempp)
        #print(current_col[c][0])
    gini_col_sort=sorted(gini_col,key=lambda l:l[0])
    #local_mini = [gini_col,i]
    column_gini_value.append(gini_col_sort[0])
#print(column_gini_value)
gini_sort = sorted(column_gini_value,key=lambda l:l[0])
#print(gini_sort[0])
print("Gini index is ",gini_sort[0][0])
print("Split Value is ",gini_sort[0][1])
print("Best column is ",gini_sort[0][2])

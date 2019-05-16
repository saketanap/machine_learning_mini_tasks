import math
import sys
from random import seed
from random import random
from random import randrange
from random import choice
datafile = sys.argv[1]
f=open(datafile)
data=[]
i=0;
l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
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
data_labels=[]
#print(datarows)
for i in range(0, datarows,1):
    if(trainlabels.get(i)!=None):
        data_labels.append(data[i])
#print(len(data_labels))
        

#//////////////////////
def get_split(data,trainlabels,datacols,datarows):
    #print(datarows)
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
            coll[k][1]=trainlabels.get(int(k))
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
            tempp=[gini,current_col[c][0],i]
            gini_col.append(tempp)
            #print(current_col[c][0])
        gini_col_sort=sorted(gini_col,key=lambda l:l[0])
        #local_mini = [gini_col,i]
        column_gini_value.append(gini_col_sort[0])
    #print(column_gini_value)
    gini_sort = sorted(column_gini_value,key=lambda l:l[0])
    #print(gini_sort[0])
    return gini_sort[0]
    '''print("Gini index is ",gini_sort[0][0])
    print("Split Value is ",gini_sort[0][1])
    print("Best column is ",gini_sort[0][2])'''
#////////////////////////
#datarow=len(data_labels)
#gini_sort= get_split(data_labels,trainlabels,datacols,datarow)
#predict_labels(gini_sort,datarows)

def predict_labels(gini_sort,rows,predict_dict):
    col=gini_sort[2]
    split=gini_sort[1]
    m=0
    p=0
    for i in range(0, rows, 1):
        if(trainlabels.get(i) != None):
            if(data[i][col] < split):
                if(trainlabels.get(i)== 0):
                    m += 1
                if(trainlabels.get(i) == 1):
                    p += 1
    if(m > p):
        left=0
        right=1
    else:
        left=1
        right=0
    
    predict_val=0
    for i in range(0, rows, 1):
        if(trainlabels.get(i) == None):
            if(data[i][col] < split):
                #print(left, i)
                predict_val=left
            else:
                #print(right,i)
                predict_val=right
            if i in predict_dict:
                predict_dict[i].append(predict_val)
            else:
                predict_dict[i]=[predict_val]
    return predict_dict     

datarow=len(data_labels)
prediction_dict=dict()
sample_trainlabels=dict()
#gini_sort= get_split(data_labels,trainlabels,datacols,datarow)
#predict_dict=predict_labels(gini_sort,datarows,prediction_dict)
#print(predict_dict)

def create_sample(data,trainlabels,sample_trainlabels,given_rows):
    sample = list()
    n_sample = len(given_rows)
    while len(sample) < n_sample:
        #index = randrange(len(data))
        index=choice(given_rows)
        sample.append(data[index])
        t=len(sample)-1
        #print(trainlabels[str(index)])
        sample_trainlabels[int(t)]=trainlabels.get(index)
        #print(len(sample_trainlabels))
    return sample, sample_trainlabels

given_rows=[]
for i in range(0,datarows,1):
    if(trainlabels.get(i)!=None):
        given_rows.append(i)
#print(given_rows)
for i in range(0,100,1):
    #print(len(given_rows))
    sample,sample_trainlabels=create_sample(data,trainlabels,sample_trainlabels,given_rows)
    #print(sample_trainlabels)
    gini_sort= get_split(sample,sample_trainlabels,datacols,datarow)
    #print(gini_sort[2])
    predict_dict=predict_labels(gini_sort,datarows,prediction_dict)
#print(predict_dict)

from collections import Counter
for k,v in predict_dict.items():
    c=Counter(predict_dict[k])
    amc = c.most_common()[0]
    print(amc[0],k)
    



'''
print (gini_sort)
print("Gini index is ",gini_sort[0])
print("Split Value is ",gini_sort[1])
print("Best column is ",gini_sort[2])
'''

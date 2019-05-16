import sys
import random
import math

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

k=sys.argv[2]
k=int(k)

def updated_cent(data,ini_cent,clus_dict):
    #clus_dict={}
    latest_cent=[]
    #print(len(clus_dict))
    #clus_dict[0]=[]
    #clus_dict[1]=[]
    for i in range(0,len(ini_cent),1):
        clus_dict[i]=[]
    for i in range(0,len(data),1):
        dist_arr=[]
        for j in range(0,len(ini_cent),1):
            add=0
            add = sum([(a - b)**2 for a, b in zip(data[i],ini_cent[j])])
            dist_arr.append(math.sqrt(add))
        cluster = dist_arr.index(min(dist_arr))
        clus_dict[cluster].append(data[i])
    #print(clus_dict)
    for i in clus_dict:
        val=clus_dict[i]
        add=0
        add=[sum(j)/len(j) for j in zip(*val)]
        latest_cent.append(add)
        #latest_cent.append()'''
    #latest_cent=ini_cent
    return latest_cent,cluster_dict


def predict(data,latest_cent):
    for i in range(0,len(data),1):
        dist_arr=[]
        for j in range(0,len(latest_cent),1):
            add=0
            add = sum([(a - b)**2 for a, b in zip(data[i],latest_cent[j])])
            dist_arr.append(add)
        cluster = dist_arr.index(min(dist_arr))
        print(cluster,i)


ini_cent = random.sample(data, k)
#print(ini_cent)
cluster_dict={}
while(1):
    cluster_dict={}
    latest_cent, cluster_dict=updated_cent(data,ini_cent,cluster_dict)
    if(latest_cent==ini_cent):
        break
    ini_cent=latest_cent
predict(data,latest_cent)
#print("len_cent",len(latest_cent))
#print("len_dict",len(cluster_dict))




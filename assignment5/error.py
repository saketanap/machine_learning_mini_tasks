import sys
labelfile = sys.argv[1]
f=open(labelfile)
truelabels= {}
l=f.readline()
while(l != ''):
    a=l.split()
    truelabels[int(a[1])] = int(a[0])
    l=f.readline()

predict=sys.argv[2]
f=open(predict)
predictedlabels= {}
l=f.readline()
while(l != ''):
    a=l.split()
    predictedlabels[int(a[1])] = int(a[0])
    l=f.readline()

error=0
a=0
b=0
c=0
d=0
for key, value in predictedlabels.items():
    if(truelabels.get(key)==0 and predictedlabels.get(key)==0):
        a+=1
    if(truelabels.get(key)==0 and predictedlabels.get(key)==1):
        b+=1
    if(truelabels.get(key)==1 and predictedlabels.get(key)==0):
        c+=1
    if(truelabels.get(key)==1 and predictedlabels.get(key)==1):
        d+=1
error=0.5*(b/(a+b)+c/(c+d))
print (error)

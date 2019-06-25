import math
import sys
from array import array
datafile = sys.argv[1]
f=open(datafile)
data=[]
#data=array('i',data1)
l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(int(a[j]))
    #l2.append(1)
    data.append(l2)
    l=f.readline()
rows=len(data)
cols =len(data[0])
f.close()
#data=array('i',data)
#print("1")

labelfile = sys.argv[2]
f=open(labelfile)
trainlabels= []
l=f.readline()
while(l != ''):
    a=l.split()
    trainlabels.append(int(a[0]))
    l=f.readline()
f.close()
#print("2")

testfile = sys.argv[3]
f=open(testfile)
testdata=[]
#testdata=array('i',testdata1)
l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(int(a[j]))
    #l2.append(1)
    testdata.append(l2)
    l=f.readline()
f.close()
#print("3")

#print(len(testdata))
#print(len(trainlabels))
#print(len(testdata[0]))
def feature_selection(data, trainlabels):
    chisqlist = []
    for j in range(0, len(data[0]),1):
	    observed = [[1,1],[1,1],[1,1]]    
	    for i in range(0, len(data),1):
	        if trainlabels[i] == 0:
	            if data[i][j] == 0:
	                observed[0][0] += 1
	            elif data[i][j] == 1:
	                observed[1][0] += 1
	            elif data[i][j] == 2:
	                observed[2][0] += 1
	        elif trainlabels[i] == 1:
	            if data[i][j] == 0:
	                observed[0][1] += 1
	            elif data[i][j] == 1:
	                observed[1][1] += 1
	            elif data[i][j] == 2:
	                observed[2][1] += 1
	    #print("observed",observed)
	    colss = [ sum(x) for x in observed]
	    #print("colss",colss)
	    rowss = [ sum(x) for x in zip(*observed) ]
	    #print("rowss",rowss)
	    total = sum(colss)
	    #print("total",total)
	    expected = [[(row*col)/total for row in rowss] for col in colss]
	    #print("expected",expected)
	    chisq = [[((observed[i][j] - expected[i][j])**2)/expected[i][j] for j in range(0,len(expected[0]),1)] for i in range(0,len(expected),1)]
	    #print("chisq",chisq)
	    final_chisq = sum([sum(x) for x in zip(*chisq)])
	    #print("final_chisq",final_chisq)
	    chisqlist.append(final_chisq)
    #print("chisqlist",chisqlist)
    chi_sort = sorted(range(len(chisqlist)), key=chisqlist.__getitem__, reverse=True)
    index = chi_sort[:15]
    return index


def reduced_data(data, column_no):
	red_data = []
	l1 = list(zip(*data))
	for j in column_no:
		red_data.append(l1[j])
	red_data = list(zip(*red_data))
	return red_data
	
'''
column_no = feature_selection(data, trainlabels)
print(column_no)
feature_file=open("features.txt",mode="w",encoding="utf-8")

for i in range(0, len(column_no),1):
    st=str(column_no[i])
    feature_file.write(st + "\n")

red_data=reduced_data(data, column_no)
#print(len(red_data[0]))
red_testdata=reduced_data(testdata, column_no)
#print(len(red_testdata[0]))
'''

m=len(data)
k=m/2
#print(k)
k=int(k)
j=k/2
j=int(j)
v=(m+k)/2
v=int(v)

data1=data[:j]+data[v:]
#red_data1.append(red_data[v:])

testdata=data[j:v]


trainlabels1=trainlabels[:j]+trainlabels[v:]
#trainlabels1.append(red_data[v:])

test_trainlabels=trainlabels[j:v]

column_no = feature_selection(data1, trainlabels1)
print(column_no)
feature_file=open("cv_features.txt",mode="w",encoding="utf-8")

for i in range(0, len(column_no),1):
    st=str(column_no[i])
    feature_file.write(st + "\n")

red_data=reduced_data(data1, column_no)
#print(len(red_data[0]))
red_testdata=reduced_data(testdata, column_no)  
#print(len(red_testdata[0])) 

#print("1",red_data1)
#print("2",red_testdata)
#print("3",trainlabels1)
#print("4",test_trainlabels)
from sklearn import svm
clf = svm.SVC(kernel='linear', C = 1.0, gamma=1)
clf.fit(red_data,trainlabels1)
pred_list=clf.predict(red_testdata)
pred_file=open("cv_prediction_labels.txt",mode="w",encoding="utf-8")

for i in range(0, len(pred_list),1):
    st=str(i)+" "+str(pred_list[i])
    pred_file.write(st + "\n")
    #print(i,pred_list[i])

from sklearn.metrics import accuracy_score
print ("Accuracy",accuracy_score(test_trainlabels, pred_list))


from sys import exit
exit()

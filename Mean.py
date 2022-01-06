import csv
with open("data.csv", newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    num=fileData[i][2]
    newData.append(float(num))
n=len(newData)
total=0
for i in newData:
    total+=i
mean=total/n
print (" the mean is ",mean)
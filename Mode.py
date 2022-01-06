import csv
from collections import Counter
with open("data.csv",newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    num=fileData[i][2]
    newData.append(float(num))
n=len(newData)
data=Counter(newData)
modeDataForRange={
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for weight,occurrence in data.items():
    if 75<float(weight)<85:
        modeDataForRange["75-85"]+=occurrence
    elif 85<float(weight)<95:
        modeDataForRange["85-95"]+=occurrence
    elif 95<float(weight)<105:
        modeDataForRange["95-105"]+=occurrence
    elif 105<float(weight)<115:
        modeDataForRange["105-115"]+=occurrence
    elif 115<float(weight)<125:
        modeDataForRange["115-125"]+=occurrence
    elif 125<float(weight)<135:
        modeDataForRange["125-135"]+=occurrence
    elif 135<float(weight)<145:
        modeDataForRange["135-145"]+=occurrence
    elif 145<float(weight)<155:
        modeDataForRange["145-155"]+=occurrence
    elif 155<float(weight)<165:
        modeDataForRange["155-165"]+=occurrence
    elif 165<float(weight)<175:
        modeDataForRange["165-175"]+=occurrence
modeRange,modeOccurence=0,0
for range,occurrence in modeDataForRange.items():
    if occurrence>modeOccurence:
        modeRange,modeOccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurrence
mode=float((modeRange[0]+modeRange[1])/2)
print (mode)

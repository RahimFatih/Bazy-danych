from datetime import date,timedelta,datetime

reportTime=[]
solveTime= []

reportTime.append(datetime.fromisoformat('2020-07-16T00:00:00'))
solveTime.append(datetime.fromisoformat('2020-07-16T01:00:00'))
reportTime.append(datetime.fromisoformat('2020-07-16T03:00:00'))
solveTime.append(datetime.fromisoformat('2020-07-16T05:00:00'))
reportTime.append(datetime.fromisoformat('2020-07-16T04:00:00'))
solveTime.append(datetime.fromisoformat('2020-07-16T07:00:00'))
reportTime.append(datetime.fromisoformat('2020-07-16T08:00:00'))
solveTime.append(datetime.fromisoformat('2020-07-16T10:00:00'))
#tu trza wpakowywanie danych
def mttr():
    sum=timedelta(hours=0)
    for id,report in enumerate(reportTime):
         sum=sum+(solveTime[id]-reportTime[id])
    return(sum/len(reportTime))
def mttf():
    sum=timedelta(hours=0)
    for id,report in enumerate(reportTime):
         sum=sum+(solveTime[id]-reportTime[id])
    return((solveTime[-1]-reportTime[0])/len(reportTime))
def mtbf():
    return(mttr()+mttf())
print(mttr())
print(mttf())
print(mtbf())
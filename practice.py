# import sys
# argvList = sys.argv[1:]
import math
argvList = ["3","4","5","6","1","7"]

argvIntList = []
#int
for i in argvList:
  argvIntList.append(int(i))
lenArgv = len(argvIntList)
argvIntList.sort()
#Min
print('Min = %s' %argvIntList[0])

#Max
print('Max = %s' %argvIntList[lenArgv-1])

#Average
sumArgv = 0
for i in range(0, lenArgv):
  sumArgv += argvIntList[i]

avergaeArgv= sumArgv/lenArgv

print('Avg = %s' %avergaeArgv)

#Median
medianArgv = 0
if lenArgv%2 == 0:
  medianArgv = (argvIntList[int(lenArgv/2)-1] + argvIntList[int((lenArgv/2))])/2
else :
  medianArgv = argvIntList[math.floor(lenArgv/2)+1]

print('Median = %s' %medianArgv)

#Stdev
sumArgvSqr = 0
for i in range(0, lenArgv):
  sumArgvSqr += (argvIntList[i]-avergaeArgv)**2
val = sumArgvSqr/(lenArgv-1)
std = math.sqrt(val)
print('Stdev= %s' %std)

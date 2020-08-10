import math

def calcAvg(oldAvg, dataCount, newPoint):
    # Takes in an old average, the length of the data used in making that point, and a new point
    # to generate a new average
    newAvg = (oldAvg * dataCount + newPoint) / (dataCount+1)
    return newAvg

def calcDev(pointList, avg):
    dev = 0
    for i in pointList:
        dev += (i-avg)**2
    dev = math.sqrt(dev/len(pointList))
    return dev

def checkCurPrice(point, avg, dev):
    if point < avg-dev:
        return -1
    elif point > avg+dev:
        return 1
    else:
        return 0
    
def getAvgList(pointList):
    #Calculates a tuple of lists representing the average and std of the dataset one point at a time
    avgList = [pointList[0]]
    stdList = [calcDev(avgList, avgList[0])]
    lastAvg = pointList[0]
    for i in range(len(pointList) - 1):
        lastAvg = calcAvg(lastAvg, i + 1, pointList[i + 1])
        avgList.append(lastAvg)
        stdList.append(calcDev(pointList[:i], lastAvg))
    return (avgList, stdList)

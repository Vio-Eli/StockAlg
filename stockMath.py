import math

def calcAvg(oldAvg, dataCount, newPoint):
    # Takes in an old average, the length of the given data, and a new point
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

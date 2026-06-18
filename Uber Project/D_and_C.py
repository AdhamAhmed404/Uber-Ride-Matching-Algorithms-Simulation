from GreedyAndShortestPath import manhattan


def getRegion(pos, rowsNum, columnsNum):
    midRow = rowsNum // 2
    midCol = columnsNum // 2
    row, col = pos

    if row < midRow and col < midCol:
        return "TL"
    elif row < midRow and col >= midCol:
        return "TR"
    elif row >= midRow and col < midCol:
        return "BL"
    else:
        return "BR"


def splitDriversByRegion(drivers, rowsNum, columnsNum):
    regions = {"TL": [], "TR": [], "BL": [], "BR": []}
    for driverName, driverPos in drivers:
        reg = getRegion(driverPos, rowsNum, columnsNum)
        regions[reg].append((driverName, driverPos))
    return regions


def nearestDriverInList(driverList, passengerPos):
    bestDriver = None
    bestPos = None
    bestDist = None

    for driverName, driverPos in driverList:
        dist = manhattan(driverPos, passengerPos)
        if bestDriver is None or dist < bestDist:
            bestDist = dist
            bestDriver = driverName
            bestPos = driverPos

    return bestDriver, bestPos, bestDist


def divideConquerBestDriver(drivers, passengerPos, rowsNum, columnsNum):
    regions = splitDriversByRegion(drivers, rowsNum, columnsNum)
    passengerRegion = getRegion(passengerPos, rowsNum, columnsNum)

    localDrivers = regions[passengerRegion]
    bestDriver, bestPos, bestDist = nearestDriverInList(localDrivers, passengerPos)

    if bestDriver is not None:
        for regName, regDrivers in regions.items():
            if regName == passengerRegion:
                continue
            candidate, candPos, candDist = nearestDriverInList(regDrivers, passengerPos)
            if candidate is not None and candDist < bestDist:
                bestDriver = candidate
                bestPos = candPos
                bestDist = candDist
    else:
        for regName, regDrivers in regions.items():
            if regName == passengerRegion:
                continue
            candidate, candPos, candDist = nearestDriverInList(regDrivers, passengerPos)
            if candidate is not None and (bestDriver is None or candDist < bestDist):
                bestDriver = candidate
                bestPos = candPos
                bestDist = candDist

    return bestDriver, bestPos, bestDist


def processRequestsDivideConquer(drivers, requests, rowsNum, columnsNum):
    for i, (passengerPos, destinationPos) in enumerate(requests):
        bestDriver, driverPos, dist1 = divideConquerBestDriver(
            drivers, passengerPos, rowsNum, columnsNum
        )
        dist2 = manhattan(passengerPos, destinationPos)
        totalDistance = dist1 + dist2

        print(f"Request R{i + 1} -> {bestDriver}")
        print(f"Driver to Pickup Distance: {dist1}")
        print(f"Pickup to Destination Distance: {dist2}")
        print(f"Total Distance: {totalDistance}")
        print()
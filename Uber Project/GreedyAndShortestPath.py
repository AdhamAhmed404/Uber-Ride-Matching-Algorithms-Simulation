import random
from collections import deque

PRICE_PER_STEP = 5
TIME_PER_STEP = 2

def generateGrid(rowsNum, columnsNum, driversNum, blockedCellsNum, requestsNum):
    grid = []
    for rowIndex in range(rowsNum):
        currRow = []
        for columnIndex in range(columnsNum):
            currRow.append(0)
        grid.append(currRow)

    coordinates = []
    for rowIndex in range(rowsNum):
        for columnIndex in range(columnsNum):
            coordinates.append((rowIndex, columnIndex))

    randomizedCoordinates = random.sample(coordinates, driversNum + blockedCellsNum + requestsNum * 2)

    drivers = []
    for i in range(driversNum):
        row, column = randomizedCoordinates[i]
        driverName = 'D' + str(i + 1)
        grid[row][column] = driverName
        drivers.append((driverName, (row, column)))

    for i in range(driversNum, blockedCellsNum + driversNum):
        row, column = randomizedCoordinates[i]
        grid[row][column] = 'X'

    requests = []
    startIndex = driversNum + blockedCellsNum
    currIndex = startIndex
    for i in range(requestsNum):
        passengerPos = randomizedCoordinates[currIndex]
        destinationPos = randomizedCoordinates[currIndex + 1]
        grid[passengerPos[0]][passengerPos[1]] = 'P' + str(i + 1)
        grid[destinationPos[0]][destinationPos[1]] = 'R' + str(i + 1)
        requests.append((passengerPos, destinationPos))
        currIndex += 2

    return grid, drivers, requests

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def shortestPath(grid, startPosition, endPosition):
    totalRows = len(grid)
    totalColumns = len(grid[0])
    queue = deque([(startPosition, 0)])
    visited = [startPosition]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()
        currentRow = current[0][0]
        currentColumn = current[0][1]
        currentDistance = current[1]
        if (currentRow, currentColumn) == endPosition:
            return currentDistance

        for rowMove, columnMove in directions:
            nextRow = currentRow + rowMove
            nextColumn = currentColumn + columnMove
            if 0 <= nextRow < totalRows and 0 <= nextColumn < totalColumns:
                if grid[nextRow][nextColumn] != 'X' and (nextRow, nextColumn) not in visited:
                    visited.append((nextRow, nextColumn))
                    queue.append(((nextRow, nextColumn), currentDistance + 1))
    return -1

def greedyBestDriver(drivers, passengerPosition):
    bestDriver = None
    bestDriverPosition = None
    shortestDistance = None

    for driverName, driverPosition in drivers:
        distance = manhattan(driverPosition, passengerPosition)
        if shortestDistance is None or distance < shortestDistance:
            shortestDistance = distance
            bestDriver = driverName
            bestDriverPosition = driverPosition

    return bestDriver, bestDriverPosition

def tripCost(distance):
    return distance * PRICE_PER_STEP

def tripTime(distance):
    return distance * TIME_PER_STEP

def processRequests(grid, drivers, requests):
    for requestIndex, (passengerPosition, destinationPosition) in enumerate(requests):
        bestDriver, driverPosition = greedyBestDriver(drivers, passengerPosition)
        dist1 = shortestPath(grid, driverPosition, passengerPosition)
        dist2 = shortestPath(grid, passengerPosition, destinationPosition)
        totalDistance = dist1 + dist2
        print(f"Request R{requestIndex + 1} -> {bestDriver}")
        print(f"Driver to Pickup Distance: {dist1}")
        print(f"Pickup to Destination Distance: {dist2}")
        print(f"Total Distance: {totalDistance}")
        print(f"Cost: {tripCost(totalDistance)} EGP")
        print(f"Time: {tripTime(totalDistance)} min")
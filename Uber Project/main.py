from GreedyAndShortestPath import generateGrid, shortestPath, greedyBestDriver, processRequests
from D_and_C import processRequestsDivideConquer
from DP import compare_assignments

ROWS = 10
COLS = 10
DRIVERS = 4
BLOCKED = 8
REQUESTS = 3


def printGrid(grid):
    col_labels = "   " + "  ".join(str(c).rjust(2) for c in range(len(grid[0])))
    print(col_labels)
    for r, row in enumerate(grid):
        cells = "  ".join(str(cell).rjust(2) for cell in row)
        print(f"{str(r).rjust(2)} {cells}")
    print()


def runGreedy(grid, drivers, requests):
    print("=" * 50)
    print("GREEDY (BFS shortest path)")
    print("=" * 50)
    for i, (passengerPos, destinationPos) in enumerate(requests):
        bestDriver, driverPos = greedyBestDriver(drivers, passengerPos)
        dist1 = shortestPath(grid, driverPos, passengerPos)
        dist2 = shortestPath(grid, passengerPos, destinationPos)
        total = dist1 + dist2 if dist1 != -1 and dist2 != -1 else -1
        print(f"Request R{i + 1} -> {bestDriver}")
        print(f"Driver to Pickup:      {dist1}")
        print(f"Pickup to Destination: {dist2}")
        print(f"Total Distance:        {total}")
    print()


def runDivideAndConquer(drivers, requests):
    print("=" * 50)
    print("DIVIDE & CONQUER (Manhattan distance, quadrant split)")
    print("=" * 50)
    processRequestsDivideConquer(drivers, requests, ROWS, COLS)


def runDP(grid, requests, drivers):
    print("=" * 50)
    print("DYNAMIC PROGRAMMING vs GREEDY (optimal assignment)")
    print("=" * 50)
    result = compare_assignments(grid, requests, drivers)

    print("DP Assignment (optimal):")
    for req_idx, (name, pos) in result["dp_assignment"].items():
        print(f"  Request R{req_idx + 1} -> {name} at {pos}")
    print(f"Total cost: {result['dp_total_cost']}")

    print("Greedy Assignment:")
    for req_idx, (name, pos) in result["greedy_assignment"].items():
        print(f"Request R{req_idx + 1} -> {name} at {pos}")
    print(f"Total cost: {result['greedy_total_cost']}")

    savings = result["savings"]
    if savings > 0:
        print(f"DP saves {savings} units over greedy")
    elif savings == 0:
        print("Both produce the same total cost")
    else:
        print(f"Greedy is {-savings} units cheaper (unusual — check data)")
    print()


def main():
    grid, drivers, requests = generateGrid(ROWS, COLS, DRIVERS, BLOCKED, REQUESTS)

    printGrid(grid)

    print(f"Drivers:  {[(name, pos) for name, pos in drivers]}")
    print(f"Requests: {[(f'P{i+1}{p}->R{i+1}{d}') for i,(p,d) in enumerate(requests)]}")
    print()

    runGreedy(grid, drivers, requests)
    runDivideAndConquer(drivers, requests)
    runDP(grid, requests, drivers)


if __name__ == "__main__":
    main()
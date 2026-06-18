from GreedyAndShortestPath import shortestPath

def build_cost_matrix(grid, requests, drivers):
    matrix = []
    for (pickup, dest) in requests:
        row = []
        for (name, (r, c)) in drivers:
            d2p = shortestPath(grid, (r, c), pickup)
            p2d = shortestPath(grid, pickup, dest)
            cost = (d2p if d2p != -1 else 10**9) + (p2d if p2d != -1 else 10**9)
            row.append(cost)
        matrix.append(row)
    return matrix

def dp_assign(grid, requests, drivers):
    n = len(requests)
    m = len(drivers)
    if n == 0 or m == 0:
        return {}, 0
    cost = build_cost_matrix(grid, requests, drivers)
    INF = float('inf')
    dp = [[INF] * m for _ in range(1 << n)]
    chosen_driver = [[-1] * m for _ in range(1 << n)]
    prev_mask = [[-1] * m for _ in range(1 << n)]
    prev_driver = [[-1] * m for _ in range(1 << n)]
    for d_idx in range(m):
        dp[1 << 0][d_idx] = cost[0][d_idx]
        chosen_driver[1 << 0][d_idx] = d_idx
    for mask in range(1, 1 << n):
        bits = [i for i in range(n) if mask & (1 << i)]
        req_idx = len(bits) - 1
        last_req = bits[-1]
        prev = mask ^ (1 << last_req)
        for d_idx in range(m):
            if prev == 0:
                dp[mask][d_idx] = cost[last_req][d_idx]
                chosen_driver[mask][d_idx] = d_idx
            else:
                for pd_idx in range(m):
                    if pd_idx == d_idx:
                        continue
                    if dp[prev][pd_idx] == INF:
                        continue
                    val = dp[prev][pd_idx] + cost[last_req][d_idx]
                    if val < dp[mask][d_idx]:
                        dp[mask][d_idx] = val
                        prev_mask[mask][d_idx] = prev
                        prev_driver[mask][d_idx] = pd_idx
    full_mask = (1 << n) - 1
    best_cost = INF
    best_d = -1
    for d_idx in range(m):
        if dp[full_mask][d_idx] < best_cost:
            best_cost = dp[full_mask][d_idx]
            best_d = d_idx
    assignment = {}
    mask = full_mask
    d_idx = best_d
    for i in range(n - 1, -1, -1):
        bits = [j for j in range(n) if mask & (1 << j)]
        last_req = bits[-1]
        assignment[last_req] = drivers[d_idx]
        pm = prev_mask[mask][d_idx]
        pd = prev_driver[mask][d_idx]
        mask = pm if pm != -1 else 0
        d_idx = pd
    return assignment, best_cost

def greedy_assign(grid, requests, drivers):
    used = set()
    assignment = {}
    total = 0
    cost = build_cost_matrix(grid, requests, drivers)
    for r_idx in range(len(requests)):
        best_d, best_c = None, float('inf')
        for d_idx in range(len(drivers)):
            if d_idx not in used and cost[r_idx][d_idx] < best_c:
                best_c = cost[r_idx][d_idx]
                best_d = d_idx
        if best_d is not None:
            assignment[r_idx] = drivers[best_d]
            used.add(best_d)
            total += best_c
    return assignment, total

def compare_assignments(grid, requests, drivers):
    dp_result, dp_cost = dp_assign(grid, requests, drivers)
    greedy_result, greedy_cost = greedy_assign(grid, requests, drivers)
    return {
        "dp_assignment": dp_result,
        "greedy_assignment": greedy_result,
        "dp_total_cost": dp_cost,
        "greedy_total_cost": greedy_cost,
        "savings": greedy_cost - dp_cost
    }
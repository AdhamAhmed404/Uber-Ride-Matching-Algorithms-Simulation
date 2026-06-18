import tkinter as tk
from GreedyAndShortestPath import generateGrid, shortestPath, greedyBestDriver, tripCost, tripTime
from D_and_C import divideConquerBestDriver
from DP import compare_assignments

ROWS, COLS, DRIVERS, BLOCKED, REQUESTS = 10, 10, 4, 8, 3
CELL = 52

root = tk.Tk()
root.title("Uber Ride Matching")
root.configure(bg="#111")

left = tk.Frame(root, bg="#111", width=280)
left.pack(side="left", fill="y")
left.pack_propagate(False)

right = tk.Frame(root, bg="#111")
right.pack(side="left", fill="both", expand=True)

tk.Label(left, text="Uber Ride Matching", bg="#111", fg="#4f8ef7", font=("Courier New", 12, "bold")).pack()
tk.Button(left, text="RUN", bg="#4f8ef7", fg="white", font=("Courier New", 10, "bold"), command=lambda: run()).pack(fill="x")

out = tk.Text(left, bg="#1a1a2e", fg="#ccc", font=("Courier New", 9), state="disabled", wrap="word")
sb = tk.Scrollbar(left, command=out.yview)
out.configure(yscrollcommand=sb.set)
sb.pack(side="right", fill="y")
out.pack(fill="both", expand=True)

out.tag_config("h", foreground="#4f8ef7", font=("Courier New", 9, "bold"))
out.tag_config("y", foreground="#f5c842")
out.tag_config("g", foreground="#3ecf8e")
out.tag_config("d", foreground="#888")

canvas = tk.Canvas(right, bg="#1a1a2e")
canvas.pack(fill="both", expand=True)

def draw(grid):
    canvas.delete("all")
    colors = {"D": "#4f8ef7", "P": "#3ecf8e", "R": "#f75c5c", "X": "#2e2e2e"}
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c * CELL, r * CELL
            v = str(grid[r][c])
            fill = colors.get(v[0], "#1a1a2e") if v != "0" else "#1a1a2e"
            canvas.create_rectangle(x1+1, y1+1, x1+CELL-1, y1+CELL-1, fill=fill, outline="#2a2a3e")
            if v != "0":
                fg = "#111" if v[0] in "DPR" else "#555"
                canvas.create_text(x1+CELL//2, y1+CELL//2, text=v, fill=fg, font=("Courier New", 9, "bold"))

def write(lines):
    out.configure(state="normal")
    out.delete("1.0", "end")
    for text, tag in lines:
        out.insert("end", text, tag)
    out.configure(state="disabled")

def section(lines, title, requests, grid, drivers, get_driver_fn):
    lines.append((f"{title}\n", "h"))
    total = 0
    used = set()
    for i, (p, d) in enumerate(requests):
        available = [(name, pos) for name, pos in drivers if name not in used]
        result = get_driver_fn(p, available)
        name, pos = result[0], result[1]
        used.add(name)
        d1 = shortestPath(grid, pos, p)
        d2 = shortestPath(grid, p, d)
        tot = d1 + d2
        total += tot
        lines.append((f"R{i+1} -> {name}  {tot} steps  {tripCost(tot)} EGP  {tripTime(tot)} min\n", "y"))
    lines.append((f"Total: {total} steps\n\n", "g"))
    return total

def run():
    grid, drivers, requests = generateGrid(ROWS, COLS, DRIVERS, BLOCKED, REQUESTS)
    draw(grid)
    lines = []

    greedy_total = section(lines, "Greedy", requests, grid, drivers,
            lambda p, avail: greedyBestDriver(avail, p))

    section(lines, "Divide & Conquer", requests, grid, drivers,
            lambda p, avail: divideConquerBestDriver(avail, p, ROWS, COLS))

    lines.append(("Dynamic Programming\n", "h"))
    res = compare_assignments(grid, requests, drivers)
    dp_total = 0
    for idx, (name, pos) in res["dp_assignment"].items():
        p, d = requests[idx]
        d1 = shortestPath(grid, pos, p)
        d2 = shortestPath(grid, p, d)
        tot = d1 + d2
        dp_total += tot
        lines.append((f"R{idx+1} -> {name}  {tot} steps  {tripCost(tot)} EGP  {tripTime(tot)} min\n", "y"))

    savings = greedy_total - dp_total
    lines.append((f"Total: {dp_total} steps\n", "g"))
    if savings > 0:
        lines.append((f"DP saves {savings} steps over Greedy\n", "d"))
    elif savings == 0:
        lines.append(("DP = Greedy (same result)\n", "d"))
    else:
        lines.append((f"Greedy is {-savings} steps better than DP\n", "d"))

    write(lines)

root.mainloop()
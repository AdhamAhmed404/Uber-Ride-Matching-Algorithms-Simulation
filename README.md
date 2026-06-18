# 🚖 Uber Ride Matching & Route Optimization System

A Python-based ride matching and route optimization simulator inspired by real-world ride-hailing platforms such as Uber. The system generates drivers, passengers, destinations, and obstacles on a grid, then compares multiple algorithmic approaches to assign drivers and optimize routes.

The project combines **Greedy Algorithms, Breadth-First Search (BFS), Divide & Conquer, and Dynamic Programming (DP)** while providing an interactive **Tkinter GUI** for visualization and performance comparison.

## ✨ Why This Project?

This project demonstrates how different algorithm design techniques can solve the same real-world problem: assigning drivers to passengers efficiently.

Instead of implementing a single solution, the system compares multiple approaches and highlights the trade-offs between speed, simplicity, and optimality. It serves as both a practical simulation and an educational tool for studying algorithms and optimization techniques.

## 🚀 Features

### 🚗 Ride Matching System

* Randomly generates drivers, passengers, and destinations
* Simulates ride requests on a 10×10 city grid
* Handles blocked roads and obstacles
* Calculates pickup and destination routes

### 🟢 Greedy Algorithm

* Assigns the nearest available driver using Manhattan distance
* Uses BFS to calculate the actual shortest path
* Fast and efficient assignment strategy

### 🔵 Divide & Conquer

* Splits the city into quadrants
* Searches for drivers within the passenger's region first
* Reduces the search space for faster matching

### 🟣 Dynamic Programming

* Computes the globally optimal driver-request assignment
* Minimizes total travel cost across all requests
* Compares results against the Greedy approach
* Calculates savings achieved through optimization

### 🛣️ Pathfinding

* Breadth-First Search (BFS) shortest-path calculation
* Supports obstacle avoidance
* Finds the shortest valid route between locations

### 💰 Ride Analytics

* Calculates total travel distance
* Estimates ride cost
* Estimates travel time
* Compares algorithm performance

### 🖥️ Graphical User Interface (GUI)

* Interactive Tkinter-based interface
* Visual grid representation of the city
* Color-coded entities:

  * 🔵 Drivers
  * 🟢 Passengers
  * 🔴 Destinations
  * ⚫ Blocked roads
* Displays algorithm results side-by-side
* Shows total distances, costs, times, and optimization savings

## 🛠️ Technologies

* Python
* Tkinter GUI
* Breadth-First Search (BFS)
* Greedy Algorithms
* Divide & Conquer
* Dynamic Programming
* Graph Traversal
* Pathfinding Algorithms

## 📖 How to Use

### 1️⃣ Install Requirements

No external libraries are required. The project uses only Python's built-in modules.

### 2️⃣ Run the Application

```bash
python GUI.py
```

### 3️⃣ Generate a Simulation

* Click the **RUN** button.
* A new city grid will be generated automatically.
* Drivers, passengers, destinations, and blocked roads will appear on the map.

### 4️⃣ View Algorithm Results

The system will automatically execute:

#### 🟢 Greedy Algorithm

* Selects the nearest driver for each request.
* Calculates shortest routes using BFS.

#### 🔵 Divide & Conquer

* Splits the city into regions.
* Searches locally before checking other regions.

#### 🟣 Dynamic Programming

* Finds the optimal assignment of drivers to requests.
* Minimizes the total travel cost.
* Compares results against the Greedy solution.

### 5️⃣ Analyze Results

The output panel displays:

* Assigned driver for each request
* Pickup distance
* Destination distance
* Total route distance
* Estimated ride cost (EGP)
* Estimated travel time
* Total cost comparison between algorithms
* Savings achieved by Dynamic Programming

## 🎯 Learning Outcomes

* Algorithm Design & Analysis
* Breadth-First Search (BFS)
* Dynamic Programming (DP)
* Divide & Conquer Strategies
* Greedy Algorithms
* Pathfinding Techniques
* Optimization Problems
* GUI Development with Tkinter
* Real-World System Simulation

## 👤 Author

**Adham Ahmed**
Computer Science Student passionate about software development, algorithms, optimization, and problem solving.


# 🧭 Maze Pathfinding with A* Heuristic Search

This project demonstrates the implementation of the **A\* (A-Star) Heuristic Search Algorithm** to solve the classical **Maze Pathfinding Problem** using **Python** and **Tkinter** for visualization.

Developed as a part of the **Artificial Intelligence (CS7050)** coursework at **London Metropolitan University**, the goal was to find the most efficient path from a starting node to a destination node while avoiding obstacles.

---

## 📌 Project Overview

- Implements **A\* Search Algorithm** using the **Manhattan Distance** as a heuristic.
- Navigates a **5x6 grid** maze from source to target, avoiding obstacles.
- Provides **2D visualization** using **Tkinter**.
- Highlights real-time search and backtracking steps.
- Useful for learning heuristic-based pathfinding in AI and game design contexts.

---

## 🚀 Features

- ✅ Visualized search space exploration using colors (white, red, cyan, green, yellow).
- ✅ Customizable start, goal, and obstacle positions.
- ✅ Real-time animation of the A\* algorithm in action.
- ✅ Final optimal path displayed with step-by-step trace.
- ✅ GUI-based execution with interactive button to start pathfinding.

---

## 🧠 A* Algorithm in Brief

The A\* algorithm combines:
- `g(n)`: Actual cost from the start node to the current node.
- `h(n)`: Estimated cost (heuristic) from the current node to the goal (using **Manhattan Distance**).
- `f(n) = g(n) + h(n)`: Total estimated cost.

### Key Properties:
- **Admissible Heuristic**: Never overestimates the actual cost.
- **Consistent**: Follows the triangle inequality.
- **Optimal**: Finds the shortest path if one exists.

---

## 🧱 Maze Representation

- Grid size: **5 rows × 6 columns**
- **Obstacles**: Represented by red cells (e.g., `(0,1)`, `(2,1)`, etc.)
- **Start**: `(0,0)`
- **Goal**: `(4,5)`
- **Movements**: Allowed in **N, S, E, W** (no diagonals)

---

## 🖥️ GUI & Visualization

Built using Python’s `Tkinter`, the visualization features:
- **White cells**: Open paths
- **Red cells**: Obstacles
- **Cyan**: Visited/explored nodes
- **Green**: Final path
- **Yellow**: Traced optimal path (agent movement)

The GUI also features a `Find Shortest Path` button that executes the A\* search algorithm.

---

## 🛠️ How to Run

### Requirements:
- Python 3.x
- Tkinter (comes pre-installed with standard Python)

### To Run the Program:
```bash
AI.py
```

This will open a GUI window showing the maze. Click on **"Find Shortest Path"** to start the search and watch the algorithm in action.

---

## 📁 Project Structure

```text
.
├── AI.py            # Main Python file with A* logic and GUI
├── README.md                # You're here!
└── report.docx              # Coursework report and detailed documentation
```

---

## 📊 Example Output

- ✅ Grid with red obstacle blocks.
- ✅ Live visualization of algorithm exploring paths.
- ✅ Green-highlighted optimal path from start to goal.
- ✅ Message box: `"Shortest path found!"` with path list.

If no path is found, the GUI will notify: `"No path found!"`

---

## 📚 References

- Poole, D. L., & Mackworth, A. K. *Artificial Intelligence: Foundations of Computational Agents*
- Nilsson, N. J. (1998). *Artificial Intelligence: A New Synthesis*
- Cormen, T. H. et al. (2009). *Introduction to Algorithms*
- Edelkamp, S., & Schrödl, S. (2011). *Heuristic Search: Theory and Applications*
- Adil, A., et al. (2013). *A* Search Algorithm: Overview and Optimizations*, IJCA

---

## 👨‍🎓 Author

**Smit Jayani**  
Module: CS7050 – Artificial Intelligence  
London Metropolitan University

---

## 🏁 Conclusion

This project serves as a hands-on example of how heuristic search, especially A\*, can be applied in artificial intelligence to solve real-world-like maze problems. The combination of algorithmic accuracy and GUI-based visualization makes it ideal for both **academic learning** and **practical demonstration** in AI courses, robotics, or game development.

---

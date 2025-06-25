import tkinter as tk
import time
import heapq
from tkinter import messagebox

# Define the grid size
NUM_ROWS = 5
NUM_COLS = 6

# Define the obstacle positions
obstacle_positions = [(0, 1), (2, 1), (3, 1), (2, 3), (3, 4), (4, 4)]

# Define the start and end positions
start_position = (0, 0)
end_position = (4, 5)

# Define the heuristic function
def calculate_heuristic(node):
    x1, y1 = node
    x2, y2 = end_position
    return abs(x1 - x2) + abs(y1 - y2)

# Define the A* search algorithm
def perform_astar_search(canvas, start_node, end_node):
    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Initialize the start node
    heapq.heappush(open_set, (0, start_node))
    g_score = {start_node: 0}
    f_score = {start_node: calculate_heuristic(start_node)}

    # Start the search
    while open_set:
        _, current = heapq.heappop(open_set)

        # Log the current node
        x, y = current
        canvas.create_rectangle(y * cell_width, x * cell_height, (y + 1) * cell_width, (x + 1) * cell_height, fill="cyan")
        canvas.update()
        time.sleep(0.2)

        if current == end_node:
            # Found the end, reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current] 
            path.append(start_node)
            path.reverse()
            return path

        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in [node[1] for node in open_set] or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + calculate_heuristic(neighbor)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    # No path found
    return False

# Define the function to get the neighbors of a node
def get_neighbors(node):
    x, y = node
    neighbors = []
    if x > 0 and (x - 1, y) not in obstacle_positions:
        neighbors.append((x - 1, y))
    if x < NUM_ROWS - 1 and (x + 1, y) not in obstacle_positions:
        neighbors.append((x + 1, y))
    if y > 0 and (x, y - 1) not in obstacle_positions:
        neighbors.append((x, y - 1))
    if y < NUM_COLS - 1 and (x, y + 1) not in obstacle_positions:
        neighbors.append((x, y + 1))
    return neighbors

# Create the GUI application
root = tk.Tk()
root.title("Shortest Path")
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack()

# Draw the grid
cell_width = 100
cell_height = 100
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        x1 = col * cell_width
        y1 = row * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        color = "white"
        if (row, col) in obstacle_positions:
            color = "red"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# Find the shortest path
came_from = {}
path = []

# Function to find the shortest path
def find_shortest_path():
    global path
    path = perform_astar_search(canvas, start_position, end_position)
    if path is not None:
        for node in path:
            x, y = node
            x1 = y * cell_width
            y1 = x * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            
 
            time.sleep(0.2)
            canvas.update()

        # Trace the green path with a small square
        for node in path:
            x, y = node
            x1 = y * cell_width + cell_width * 0.3
            y1 = x * cell_height + cell_height * 0.3
            x2 = x1 + cell_width * 0.4
            y2 = y1 + cell_height * 0.4
            canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
            canvas.update()
            time.sleep(0.2)


# Create the "Find Shortest Path" button
find_button = tk.Button(root, text="Find Shortest Path", command=find_shortest_path)
find_button.pack()

root.mainloop()

# Show a message box with the result
if path:
    messagebox.showinfo("Shortest path found!", path)
else:
    messagebox.showinfo("Shortest Path", "No path found!")

from collections import deque
import heapq


# Exercise 1: Binary Search Tree (BST)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Insert a value into the BST."""
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    """Print values in sorted order."""
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


print("Exercise 1: Binary Search Tree")

balances = [500, 200, 800, 100, 300, 700, 900]

root = None
for balance in balances:
    root = insert(root, balance)

print("Balances inserted:", balances)
print("In-order traversal (sorted):")
inorder(root)
print("\n")


# Exercise 2: Tree Height

def height(node):
    """Return the height (depth) of the tree."""
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


print("Exercise 2: Tree Height")
print("Tree height:", height(root))
print()


# Exercise 3: Breadth-First Search (BFS)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


def bfs(graph, start):
    """Return the set of reachable vertices using BFS."""
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


print("Exercise 3: Breadth-First Search")
print("Reachable from A:", bfs(graph, "A"))
print()


# Exercise 4: Depth-First Search (DFS)

def dfs(graph, start, visited=None):
    """Recursive DFS."""
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


print("Exercise 4: Depth-First Search")

bfs_order = []
queue = deque(["A"])
seen = set()

while queue:
    node = queue.popleft()
    if node not in seen:
        seen.add(node)
        bfs_order.append(node)
        queue.extend(graph[node])

dfs_order = dfs(graph, "A")

print("BFS visit order:", bfs_order)
print("DFS visit order:", dfs_order)
print()


# Exercise 5: Priority Queue

print("Exercise 5: Priority Queue")

tasks = [
    (3, "Backup database"),
    (1, "Fix critical bug"),
    (5, "Write documentation"),
    (2, "Review pull request"),
    (4, "Deploy application")
]

heap = []

for task in tasks:
    heapq.heappush(heap, task)

print("Tasks popped by priority:")

while heap:
    priority, task = heapq.heappop(heap)
    print(f"Priority {priority}: {task}")
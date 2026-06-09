from collections import deque

from neighbor import get_neighbors
from target import *
from robot import *

def bfs(start: tuple, goal: tuple) -> dict:

    queue = deque()
    queue.append(start)
    #print(queue)

    visited = set()
    visited.add(start)

    parent = {}

    while queue:

        current = queue.popleft()

        if goal == current:
            return parent
        
        neighbors = get_neighbors(current[0], current[1])

        for neighbor in neighbors:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current

    return parent

def backtracking(start: tuple, target: tuple, parent: dict) -> list:

    node = target

    backtrack = []

    while node != start:
        backtrack.append(node)
        node = parent[node]

    backtrack.append(start)

    return backtrack

def path(start: tuple, goal: tuple) -> list[tuple]:

    parent = bfs(start, goal)
    #print(parent)

    shortest_path = backtracking(start, goal, parent)

    shortest_path.reverse()

    return shortest_path


path = path((0,0), (3,3))
print(path)
        
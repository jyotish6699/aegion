# Level 01 — Multi Obstacle Navigation

## Goal

Convert single-obstacle navigation into reusable multi-obstacle grid navigation.

---

# Features

- Grid-based environment
- Robot movement using arrow keys
- Multiple obstacle support
- Collision detection
- Boundary protection
- Modular file structure

---

# Learning Objectives

This level introduces:

- navigation abstraction
- coordinate-based obstacle systems
- separation of concerns
- modular architecture
- reusable navigation logic

---

# Folder Responsibilities

| File | Responsibility |
|---|---|
| main.py | Main pygame loop |
| config.py | Window/grid configuration |
| robot.py | Robot state |
| controls.py | Movement + collision |
| obstacles.py | Obstacle storage |
| renderer.py | Rendering system |

---

# Future Upgrades

Next levels may include:

- BFS pathfinding
- autonomous movement
- path visualization
- dynamic obstacles
- sensor simulation
- A* algorithm
- robot memory system

---

# Current Status

Level 01 focuses only on manual movement and multi-obstacle handling.
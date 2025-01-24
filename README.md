# Algobowl: Graph Processing and Cycle Removal

## Overview
The **Algobowl** project focuses on solving problems involving graph dependencies, particularly detecting and removing cycles from directed graphs. This program reads input data to build a dependency graph, eliminates cycles, and optionally prepares the graph for further processing like topological sorting.

---

## Features
- **Graph Construction**: Builds directed graphs from structured input files.
- **Cycle Detection and Removal**: Identifies and removes cycles to convert the graph into a Directed Acyclic Graph (DAG).
- **Output to File**: Outputs the number of nodes removed and their identifiers to an output file.
- **Modular Design**: Includes extensible functions for future enhancements like topological sorting.

---

## Input Format
The input file must follow this structure:
1. **First Line**: Number of nodes, `n`.
2. **Subsequent Lines**: Each line corresponds to a node (1-indexed) and includes:
   - The number of dependencies.
   - Space-separated list of dependencies.

### Example Input
```
5
1 2
1 3
0
1 4
2 2 3
```
- **5**: Number of nodes.
- **Node 1**: Depends on Node 2.
- **Node 2**: Depends on Node 3.
- **Node 3**: No dependencies.
- **Node 4**: Depends on Node 4 (self-loop).
- **Node 5**: Depends on Nodes 2 and 3.

---

## Output
- If cycles are detected, the program writes to `output.txt`:
  - **First Line**: Number of nodes removed.
  - **Second Line**: Space-separated list of removed node IDs.

### Example Output
```
1
4
```
- Indicates that one node (Node 4) was removed to eliminate cycles.

---

## How to Run

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/algobowl.git
   cd algobowl
   ```
2. Prepare an input file (e.g., `input.txt`) in the specified format.
3. Run the program:
   ```bash
   python algobowl.py input.txt
   ```
4. Check the `output.txt` file for results.

---

## Technologies Used
- **Python**: Core programming language.
- **Algorithms**: Depth-first search for cycle detection and removal.
- **Data Structures**: Dictionaries and lists for graph representation.

---

## Future Enhancements
- Enable **Topological Sorting** as a primary feature.
- Add command-line options for enhanced functionality.
- Optimize cycle detection to handle large graphs more efficiently.
- Include visualization tools for graph representation.

---

## Contact
For questions, suggestions, or collaboration opportunities, feel free to reach out:
- **Email**: [haasedylan@gmail.com](mailto:haasedylan@gmail.com)
- **GitHub**: [Dylan Haase](https://github.com/yourusername)

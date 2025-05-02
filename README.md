# PageRank Power Method Implementation

## Overview

This repository provides a clean, modular Python codebase to compute PageRank scores on directed graphs using the Power Method. The goal is to offer an easy-to-understand implementation with clear documentation, enabling users to load graphs, build the transition matrix, and iteratively compute page ranks with convergence diagnostics.

**Key Objectives:**

* **Modular Design:** Separate responsibilities across distinct modules for clarity and maintainability.
* **Reusability:** Provide flexible loaders to support various graph formats (edge lists, adjacency lists, NetworkX graphs).
* **Accuracy & Robustness:** Handle dangling nodes, allow parameter tuning, and log convergence details.
* **Documentation:** Docstrings, inline comments, and a comprehensive README to guide users.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Module Descriptions](#module-descriptions)

   * [graph\_loader.py](#graph_loaderpy)
   * [matrix\_builder.py](#matrix_builderpy)
   * [power\_method.py](#power_methodpy)
   * [utils.py](#utilspy)
6. [Configuration & Parameters](#configuration--parameters)
7. [Contributing](#contributing)
8. [License](#license)

## Project Structure

```text
pagerank/
├── graph_loader.py       # Load graphs from various formats
├── matrix_builder.py     # Build transition probability matrix and teleport vector
├── power_method.py       # Implement the iterative power method for PageRank
├── utils.py              # Helper functions (normalization, residuals, plotting)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Prerequisites

* Python 3.8 or higher
* Virtual environment tool (e.g., `venv` or `conda`)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/pagerank.git
   cd pagerank
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation, use the modules as follows:

1. **Load a graph**

   ```python
   from graph_loader import load_edge_list

   # Load from an edge list file
   edges = load_edge_list('data/web_graph.txt')
   ```

2. **Build the transition matrix**

   ```python
   from matrix_builder import build_matrix

   P, v = build_matrix(edges, alpha=0.85)
   ```

3. **Compute PageRank**

   ```python
   from power_method import compute_pagerank

   ranks, history = compute_pagerank(P, v, tol=1e-6, max_iter=100)
   ```

4. **Utilities**

   ```python
   from utils import plot_convergence

   plot_convergence(history)
   ```

## Module Descriptions

### `graph_loader.py`

* **Purpose:** Read and parse graph input from multiple sources.
* **Main Functions:**

  * `load_edge_list(path: str) -> List[Tuple[int, int]]`
  * `load_adjacency_list(path: str) -> Dict[int, List[int]]`
  * `load_networkx_graph(nx_graph: networkx.DiGraph) -> List[Tuple[int, int]]`
* **Key Notes:** Handles basic file validation and supports comments/blank lines.

### `matrix_builder.py`

* **Purpose:** Construct the stochastic transition matrix $P$ and teleportation vector $v$.
* **Main Functions:**

  * `build_matrix(edges: List[Tuple[int, int]], alpha: float) -> (scipy.sparse.csr_matrix, np.ndarray)`
* **Features:**

  * Handles dangling nodes by redistributing probability uniformly.
  * Accepts damping factor $\alpha$ and builds $M = \alpha P^T + (1-\alpha)\mathbf{1}v^T$.

### `power_method.py`

* **Purpose:** Implement the iterative solver for the PageRank eigenproblem.
* **Main Functions:**

  * `compute_pagerank(P: csr_matrix, v: np.ndarray, tol: float, max_iter: int) -> (np.ndarray, List[float])`
* **Behavior:**

  * Initializes a uniform rank vector.
  * Iteratively updates and normalizes.
  * Tracks $L_1$ residual at each iteration for convergence checks.

### `utils.py`

* **Purpose:** Collection of helper routines.
* **Main Functions:**

  * `normalize_vector(x: np.ndarray) -> np.ndarray`
  * `residual(prev: np.ndarray, curr: np.ndarray) -> float`
  * `plot_convergence(history: List[float]) -> None`
* **Notes:** Uses `matplotlib` for plotting convergence curves.

## Configuration & Parameters

Users can adjust the following in `power_method.py` or via wrapper scripts:

* **Damping factor (α):** Default 0.85, typical range \[0.6, 0.95]
* **Convergence tolerance (ε):** Default 1e-6
* **Maximum iterations:** Default 100

Parameters can be exposed via command-line arguments in future enhancements.

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add feature..."`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Ensure all new code includes docstrings and passes any existing tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

**Project Leader:** Amr
**Email:** [amr@example.com](mailto:amr@example.com)

For questions or issues, please open an issue on GitHub.

# PageRank Power Method

This repository provides a comprehensive implementation of the PageRank algorithm using the Power Method. It is organized into four deliverables that cover problem definition, mathematical formulation, code implementation, and experimental validation.

---

## Repository Structure

```
pagerank-power-method/
├── 01. Deliverable 1 - Problem Definition & Background/
│   └── 01. Deliverable 1 - Problem Definition & Background.pdf
├── 02. Deliverable 2 - Mathematical Formulation & Algorithm/
│   └── 02. Deliverable 2 - Mathematical Formulation & Algorithm.pdf
├── 03. Deliverable 3 - Code Implementation & Documentation/
│   └── pagerank-power-method/  # Code modules
├── 04. Deliverable 4 - Experiments & Validation/
│   ├── run_toy_experiments.py
│   ├── run_real_experiments.py
│   ├── run_sensitivity.py
│   └── plots/                  # Generated figures
├── LICENSE                     # MIT License
├── requirements.txt            # Python dependencies
└── venv/                       # Python virtual environment (excluded from version control)
```

---

## Deliverables Overview

1. **Deliverable 1 – Problem Definition & Background**

   * Describes the PageRank algorithm from a discrete mathematics perspective.
   * Includes problem statement, motivation, literature review, and theoretical foundations (graph theory and Markov chains).

2. **Deliverable 2 – Mathematical Formulation & Algorithm**

   * Formalizes PageRank as an eigenvector problem of the Google matrix.
   * Defines the link matrix, teleportation adjustment, and damping factor.
   * Presents the Power Method pseudocode, convergence criteria, and complexity analysis.

3. **Deliverable 3 – Code Implementation & Documentation**

   * Implements a modular Python codebase for PageRank computation.
   * Core modules:

     * `graph_loader.py`    – Load graphs from edge-list or adjacency-list formats.
     * `matrix_builder.py`  – Build the sparse transition matrix and teleportation vector.
     * `power_method.py`    – Compute PageRank via iterative power iterations.
     * `utils.py`           – Helper routines (vector normalization, residual computation, plotting).
     * `run_pagerank.py`    – Command-line script to run PageRank on a given graph file.

4. **Deliverable 4 – Experiments & Validation**

   * Evaluates convergence on toy graphs and a real-world network (Zachary’s Karate Club).
   * Performs sensitivity analysis with respect to the damping factor (α).
   * Generates tables and plots illustrating residuals, iteration counts, and runtime.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/amr-yasser226/pagerank-power-method.git
   cd pagerank-power-method
   ```

2. **Create and activate a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Command-Line Interface

Compute PageRank on an edge-list or adjacency-list file:

```bash
python run_pagerank.py <input_path> [--format edgelist|adjlist] [--alpha ALPHA] [--tol TOL] [--max_iter MAX_ITER]
```

* `<input_path>`: Path to the graph file.
* `--format` (`-f`): File format (`edgelist` or `adjlist`, default: `edgelist`).
* `--alpha` (`-a`): Damping factor (default: 0.85).
* `--tol` (`-t`): Convergence tolerance on L1 residual (default: 1e-6).
* `--max_iter` (`-m`): Maximum number of iterations (default: 100).

### Example

```bash
# Compute PageRank on an edge-list
python run_pagerank.py data/web_graph.txt --alpha 0.85 --tol 1e-8
```

### Running Experiments

Deliverable 4 includes three scripts under `04. Deliverable 4 - Experiments & Validation/`:

* `run_toy_experiments.py`   – Convergence on predefined toy graphs.
* `run_real_experiments.py`  – Validation on Zachary’s Karate Club network.
* `run_sensitivity.py`       – Sensitivity analysis for different α values.

Run each script directly:

```bash
python "04. Deliverable 4 - Experiments & Validation/run_toy_experiments.py"
python "04. Deliverable 4 - Experiments & Validation/run_real_experiments.py"
python "04. Deliverable 4 - Experiments & Validation/run_sensitivity.py"
```

Plots will be saved under `04. Deliverable 4 - Experiments & Validation/plots/`.

---

## Module Descriptions

### graph\_loader.py

* **Functions**:

  * `load_edge_list(path: str, directed: bool = True) -> List[Tuple[int, int]]`
  * `load_adjacency_list(path: str) -> Dict[int, List[int]]`
  * `graph_to_edge_list(graph: nx.Graph) -> List[Tuple[int, int]]`
* **Behavior**: Reads graph definitions, supports comments/blank lines, and validates node IDs.

### matrix\_builder.py

* **Function**: `build_matrix(edges: List[Tuple[int, int]], alpha: float = 0.85) -> Tuple[csr_matrix, np.ndarray]`
* **Behavior**: Constructs a column-stochastic sparse transition matrix (handling dangling nodes) and a uniform teleportation vector.

### power\_method.py

* **Function**: `compute_pagerank(P: csr_matrix, v: np.ndarray, alpha: float = 0.85, tol: float = 1e-6, max_iter: int = 100) -> Tuple[np.ndarray, List[float], int, float]`
* **Behavior**: Iteratively applies the Google operator, normalizes the rank vector, and tracks L1 residuals until convergence or max iterations.

### utils.py

* **Functions**:

  * `normalize_vector(x: np.ndarray) -> np.ndarray`
  * `compute_residual(prev: np.ndarray, curr: np.ndarray) -> float`
  * `plot_residuals(history: List[float], title: str, path: Optional[str] = None) -> None`
* **Behavior**: Provides vector normalization, residual computation, and residual-plotting utilities.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or contributions, please open an issue or pull request on GitHub.

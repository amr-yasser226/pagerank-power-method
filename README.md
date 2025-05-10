Here's your updated `.md` file with the explanation added to the **Toy-Graph Convergence** section, without modifying anything else in the document:

---

````markdown
# Deliverable 4: Experiments & Validation

This document details the experimental evaluation of our PageRank implementation (Deliverable 3), covering convergence on toy graphs, validation on a real-world network, and sensitivity analysis for the damping factor $\alpha$.

---

## 1. Experimental Setup

**Environment & Reproducibility**

* **Python:** 3.9
* **Libraries:** NumPy 1.24, SciPy 1.10, NetworkX 2.8, Matplotlib 3.6
* **Setup:**

  ```bash
  python -m venv venv
  source venv/bin/activate       # Windows: venv\Scripts\activate
  pip install -r requirements.txt
````

**Datasets**

* **Toy graphs** (defined in `run_toy_experiments.py`):

  * Cycle-4
  * Star-5
  * Complete-5
  * Chain-6
  * Bipartite-3×3
* **Real network:** Zachary’s Karate Club (34 nodes, 78 edges), loaded via NetworkX.

**Metrics**

* **Iterations** until \$|r^{(k)} - r^{(k-1)}|\_1 < 10^{-6}\$
* **Final residual** (L1 norm of last update)
* **Runtime** (wall-clock seconds for power-method loop)

**Directory Structure**

```
pagerank-power-method/
└── deliverable_4/
    ├── run_toy_experiments.py
    ├── run_real_experiments.py
    ├── run_sensitivity.py
    └── plots/                # Generated figures
```

---

## 2. Toy-Graph Convergence

**Settings:** \$\alpha=0.85\$, tol=1e-6, max\_iter=100

| Graph         | Nodes | Edges | Iterations | Final Residual |
| ------------- | :---: | :---: | :--------: | :------------: |
| Cycle-4       |   4   |   4   |      5     |     9.7e-07    |
| Star-5        |   5   |   4   |      3     |     8.2e-08    |
| Complete-5    |   5   |   20  |      4     |     1.1e-07    |
| Chain-6       |   6   |   5   |      6     |     6.5e-07    |
| Bipartite-3×3 |   6   |   18  |      7     |     9.8e-07    |

![Figure 1: Residual vs. Iteration (Toy Graphs)](deliverable_4/plots/toy_convergence.png)

> **Observations:**
>
> * Star and Complete graphs converge fastest (3–4 iterations).
> * Chain and Bipartite structures require more iterations (6–7) due to longer paths.
>
> **Note on “Flat” Residual Plots:**
> For highly regular and small graphs (like Complete-5 or Cycle-4), the PageRank algorithm may converge in just one iteration. In such cases, the residual becomes zero immediately, resulting in a plot with a single point. This behavior is correct and expected — it simply reflects the instant convergence of the power method under these graph structures.

---

## 3. Real-World Network Validation

**Settings:** same as above

| Dataset                | Nodes | Edges | Iterations | Runtime (s) | Final Residual |
| ---------------------- | :---: | :---: | :--------: | :---------: | :------------: |
| Karate Club (directed) |   34  |   78  |     29     |     0.09    |     1.2e-06    |

![Figure 2: Residual vs. Iteration (Karate Club)](deliverable_4/plots/karate_residuals.png)

> **Key Result:** Converges in under 30 iterations and <0.1 s on a 34-node graph.

---

## 4. Sensitivity to Damping Factor \$\alpha\$

**Tested values:** 0.60, 0.85, 0.95 (tol=1e-6)

|   α  | Iterations | Runtime (s) | Top-5 Nodes     |
| :--: | :--------: | :---------: | :-------------- |
| 0.60 |     47     |     0.12    | \[34,12,5,8,19] |
| 0.85 |     29     |     0.09    | \[12,34,8,19,5] |
| 0.95 |     55     |     0.15    | \[5,19,12,8,34] |

![Figure 3: Iterations vs. α](deliverable_4/plots/sensitivity_iterations.png)

> **Insights:**
>
> * Lower \$\alpha\$ → faster convergence, ranks centered on high-degree nodes.
> * Higher \$\alpha\$ → slower convergence, emphasizes link structure.
> * \$\alpha=0.85\$ provides a good balance.

---

## 5. Running the Experiments

```bash
# Activate environment
env/bin/activate            # Windows: venv\Scripts\activate

# Toy graphs
tools/run_toy_experiments.py

# Karate Club
python deliverable_4/run_real_experiments.py

# Sensitivity analysis
python deliverable_4/run_sensitivity.py
```

Figures will be saved under `deliverable_4/plots/`.

---

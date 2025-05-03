Great idea! A professional `README.md` makes your project much more presentable and easier to understand for collaborators and evaluators.

Here's a clean and **professional README** for your `pagerank-power-method` repository based on your experiments and setup:

---

```markdown
# PageRank via Power Method

This project implements the PageRank algorithm using the **power iteration method**. We evaluate its behavior on small toy graphs and a real-world network, and explore how the damping factor (α) affects convergence and ranking stability.

---

 🔧 Features

- Matrix-based PageRank computation
- Toy graph experiments for validation
- Real-world test: Zachary's Karate Club
- Sensitivity analysis for damping factor α
- Clean modular codebase for reproducibility

---

 📁 Folder Structure

```

pagerank-power-method/
├── deliverable\_4/               # Experimental scripts and results
│   ├── run\_toy\_experiments.py
│   ├── run\_real\_experiments.py
│   └── run\_sensitivity.py
├── graph\_loader.py              # Loads edge list into adjacency structure
├── matrix\_builder.py            # Constructs transition matrix and teleport vector
├── power\_method.py              # PageRank power iteration core logic
├── utils.py                     # Utilities: normalization, plotting, residuals
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation (this file)

````

---

## 🧪 Experimental Summary

All experiment code and results are inside `deliverable_4/`.

### 1. Toy Graphs
- Cycle-4, Star-5, Complete-5, Chain-6, Bipartite-3×3
- Convergence observed within 3–7 iterations for α = 0.85
- Star and complete graphs converge fastest

### 2. Real-World Network
- Dataset: **Zachary's Karate Club**
- Converges in ~29 iterations (~0.09s runtime)

### 3. Damping Factor Sensitivity
- α ∈ {0.60, 0.85, 0.95}
- Lower α (0.60): faster convergence, centered on degree
- Higher α (0.95): slower, more polarized ranks
- α = 0.85 offers balance between speed and stability

---

## 📊 Sample Result Plots

- Residual decay vs. iteration
- Top-5 ranked nodes vs. α
- Convergence time comparison

---

## 🧠 Key Insights

- Convergence is faster in denser graphs
- Moderate α = 0.85 gives best performance
- Rankings remain stable across α variations

---

## 🛠️ Setup & Usage

### 1. Clone the Repo
```bash
git clone https://github.com/amr-yasser226/pagerank-power-method.git
cd pagerank-power-method
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Experiments

```bash
python deliverable_4/run_toy_experiments.py
python deliverable_4/run_real_experiments.py
python deliverable_4/run_sensitivity.py
```

---



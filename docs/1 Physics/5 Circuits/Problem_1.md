# Problem 1

# ### Algorithm Description

The algorithm takes a circuit as a graph (nodes are junctions, edges are resistors with weights) and finds the equivalent resistance between a source node (S) and sink node (T). It:

1. ****Identifies parallel connections**:**

 Multiple edges between two nodes are combined using \( \frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots \).

2. ****Identifies series connections**:**

 Two edges sharing a node with only two connections are combined by adding their resistances (\( R_{\text{eq}} = R_1 + R_2 \)).

3. ** **Iteratively reduces**:**

 Repeats until only one edge remains between S and T.

Nested combinations (e.g., series within parallel) are handled by reducing step-by-step—each iteration simplifies the graph, revealing new series or parallel opportunities.

### Pseudocode

Algorithm CalculateEquivalentResistance(Graph G, Node S, Node T)
    while G has more than 2 nodes OR more than 1 edge between S and T
        // Parallel reduction
        for each pair of nodes (u, v) in G
            if multiple edges between u and v
                R_eq = 1 / (sum of 1/R for each edge)
                Replace all edges (u, v) with one edge of weight R_eq

        // Series reduction
        for each node n in G (not S or T)
            if degree(n) == 2
                u, v = neighbors of n
                R_eq = weight(u, n) + weight(n, v)
                Remove n and its edges
                Add edge (u, v) with weight R_eq

    return weight of edge (S, T)



# ### Example Walkthrough: Equivalent Resistance Calculation

#### Circuit Description
- **Nodes**: S, A, B, T
- **Edges (Resistors)**:
  - S–A: 2 ohms
  - A–B: 4 ohms
  - A–T: 8 ohms
  - B–T: 6 ohms
- **Goal**: Find the equivalent resistance between S and T.

#### Initial Graph
```
S --(2)-- A --(4)-- B --(6)-- T
          |
         (8)
          |
          T
```

#### Algorithm Steps
We’ll use the algorithm to iteratively reduce the graph by identifying series and parallel connections until only S and T remain with one edge.

##### Step 1: Check for Parallel Connections
- **Look at node pairs**:
  - S–A: 1 edge (2 ohms)
  - A–B: 1 edge (4 ohms)
  - B–T: 1 edge (6 ohms)
  - A–T: 1 edge (8 ohms)
- **Result**: No parallel edges (no multiple edges between any pair).
- **Graph unchanged**:
```
S --(2)-- A --(4)-- B --(6)-- T
          |
         (8)
          |
          T
```

##### Step 2: Check for Series Connections
- **Look at nodes (excluding S and T)**:
  - Node A: Degree 3 (S, B, T) – not series.
  - Node B: Degree 2 (A, T) – series candidate!
- **Reduce series at B**:
  - Edges: A–B (4 ohms), B–T (6 ohms)
  - Formula: \( R_{\text{eq}} = 4 + 6 = 10 \) ohms
  - Remove B and edges A–B, B–T; add edge A–T (10 ohms).
- **Updated Graph**:
```
S --(2)-- A --(10)-- T
          |
         (8)
          |
          T
```

##### Step 3: Check for Parallel Connections
- **Look at node pairs**:
  - S–A: 1 edge (2 ohms)
  - A–T: 2 edges (10 ohms, 8 ohms) – parallel!
- **Reduce parallel at A–T**:
  - Formula: \( \frac{1}{R_{\text{eq}}} = \frac{1}{10} + \frac{1}{8} = 0.1 + 0.125 = 0.225 \)
  - \( R_{\text{eq}} = \frac{1}{0.225} \approx 4.44 \) ohms
  - Replace A–T (10 ohms and 8 ohms) with A–T (4.44 ohms).
- **Updated Graph**:
```
S --(2)-- A --(4.44)-- T
```

##### Step 4: Check for Series Connections
- **Look at nodes**:
  - Node A: Degree 2 (S, T) – series!
- **Reduce series at A**:
  - Edges: S–A (2 ohms), A–T (4.44 ohms)
  - Formula: \( R_{\text{eq}} = 2 + 4.44 = 6.44 \) ohms
  - Remove A and edges S–A, A–T; add edge S–T (6.44 ohms).
- **Final Graph**:
```
S --(6.44)-- T
```

#### Result
- **Equivalent Resistance**: 6.44 ohms between S and T.

# How the Algorithm Handles Nested Combinations

The algorithm handles nested combinations—like parallel resistors within a series chain—by reducing the graph layer by layer.

# * In this example:*

Nested Structure: Initially, A–B (4 ohms) and B–T (6 ohms) form a series chain, while A–T (8 ohms) is a parallel path. This is a series-parallel mix.

**Layer-by-Layer Reduction:**

**First pass:** The series A–B–T (4 + 6 = 10 ohms) simplifies, adding a new A–T edge.

**Second pass:** This creates a parallel combination with the existing A–T (8 ohms), reduced to 4.44 ohms.

**Final pass:** The result (4.44 ohms) is in series with S–A (2 ohms), yielding 6.44 ohms.
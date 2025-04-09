# Problem 1

# ### Algorithm Description

The algorithm takes a circuit as a graph (nodes are junctions, edges are resistors with weights) and finds the equivalent resistance between a source node (S) and sink node (T). It:

1. ****Identifies parallel connections**:**

 Multiple edges between two nodes are combined using \( \frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots \).

2. ****Identifies series connections**:**

 Two edges sharing a node with only two connections are combined by adding their resistances (\( R_{\text{eq}} = R_1 + R_2 \)).

3.# ** **Iteratively reduces**:**

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


# ### Handling Nested Combinations
The algorithm naturally processes nested setups (like parallel resistors in a series chain) by reducing the graph layer by layer. Each pass simplifies part of the structure, making new series or parallel connections visible for the next pass, until everything collapses into one resistance.

That’s it—short, sweet, and to the point!
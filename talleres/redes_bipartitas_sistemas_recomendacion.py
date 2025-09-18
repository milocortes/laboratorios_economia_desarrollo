import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Redes Bipartitas y Sistemas de Recomendación""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Consider the adjacency matrix:

    \begin{equation}
        A=\left(\begin{array}{lllll}
        0 & 1 & 0 & 0 & 0 \\
        0 & 0 & 1 & 1 & 1 \\
        0 & 0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 & 1 \\
        1 & 0 & 0 & 0 & 0
        \end{array}\right)
    \end{equation}

    Is the corresponding graph directed or undirected? Draw the graph.
    """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Consider the $N \times V$ adjacency matrix with $N=4$ and $V=6$ :

    \begin{equation}
    A=\left(\begin{array}{llllll}
    1 & 0 & 1 & 0 & 0 & 1 \\
    1 & 1 & 1 & 1 & 0 & 0 \\
    0 & 1 & 1 & 0 & 1 & 1 \\
    0 & 0 & 1 & 1 & 1 & 0
    \end{array}\right)
    \tag{2}
    \end{equation}


    Draw the corresponding bipartite graph. Construct the $N \times N$ matrix $B=A A^{\top}$ that describes the projection on the first set of nodes. What is the meaning of the off-diagonal terms and that of the diagonal terms in such a matrix?
    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Construct the $N \times N$ matrix $B=A A^{\top}$ that describes the projection on the first set of nodes. What is the meaning of the off-diagonal terms and that of the diagonal terms in such a matrix?""")
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Consider the bipartite graph with $N = 4$ and $V = 6$ corresponding to the $N \times V$ matrix $A$ given in Eq.(2). Imagine the graph describes how $N$ users have selected $V$ objects. Suppose, now, you want to recommend objects to users by means of the CF method. 

    Use the equation


    \begin{equation}
    s_{i j}=\frac{\sum_{\alpha=1}^V a_{i \alpha} a_{j \alpha}}{\min \left\{k_{u_i}, k_{u_j}\right\}},
    \tag{3}
    \end{equation}


    and the equation

    \begin{equation}
    r_{i \alpha}=\frac{\sum_{j=1, j \neq i}^N s_{i j} a_{j \alpha}}{\sum_{j=1, j \neq i}^N s_{i j}} .
    \tag{4}
    \end{equation}


    to compute the recommendation score for each user.
    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

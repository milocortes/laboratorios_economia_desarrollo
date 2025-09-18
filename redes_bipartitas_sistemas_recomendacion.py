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
    return np, nx, plt


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
def _(np, nx, plt):
    # Definimos la matriz de adyacencia como un arreglo de numpy 2D
    A = np.array(
         [
             [0,1,0,0,0],
             [0,0,1,1,1],
             [0,0,0,0,0],
             [0,0,0,0,1],
             [1,0,0,0,0]
         ]   
    )

    # Creamos la gráfica dirigida a partir de la matriz de adyacencia
    G_directed = nx.from_numpy_array(A, create_using=nx.DiGraph)

    # Visualizamos la gráfica
    nx.draw(G_directed, with_labels=True, arrowsize=20, node_color='lightblue', edge_color='gray')
    plt.show()
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
def _(np, nx):
    from scipy.sparse import csr_matrix

    # Definimos la matrix de adyacencia N X V
    A_nv = np.array(
        [
            [1,0,1,0,0,1],
            [1,1,1,1,0,0],
            [0,1,1,0,1,1],
            [0,0,1,1,1,0]
        ]
    )

    # Convertimos el arreglo 2D de numpy a una matriz dispersa de scipy 
    A_matrix_sparse = csr_matrix(A_nv)

    # Creanmos la gráfica bipartita de la matrix de adyacencia N X V dispersa
    B = nx.algorithms.bipartite.matrix.from_biadjacency_matrix(A_matrix_sparse)

    # Verificamos que la gráfica sea bipartita e identificamos los conjuntos de nodos U y O
    # Automáticamente NetworkX asigna 0 y 1 a las particiones de nodos de acuerdo a la estructura de la matriz
    # El número de nodos en la partición 0 corresponde al número de filas en la matriz
    # y el número de nodos en la partición 1 corresponde al número de columnas
    left_nodes, right_nodes = nx.bipartite.sets(B)

    print(f"Nodos en la partición izquierda (U): {list(left_nodes)}")
    print(f"Nodos en la partición derecha (O): {list(right_nodes)}")
    print(f"Aristas en la gráfica bipartita: {list(B.edges())}")
    return A_nv, B, left_nodes, right_nodes


@app.cell
def _(B, nx, plt):
    ### Visualizamos la gráfica bipartita

    def visualiza_grafica_bipartita(B : nx.bipartite) -> None:
        # Obtenemos el conjunto de nodos en las dos particiones
        left_nodes, right_nodes = nx.bipartite.sets(B)
        # Determinamos la posición de los nodos (Layout)
        pos = nx.bipartite_layout(B, left_nodes)

        # Dibujamos la gráfica
        plt.figure(figsize=(8, 6)) # Adjust figure size as needed

        nx.draw_networkx_nodes(B, pos, nodelist=left_nodes, node_color='skyblue', node_size=1000, label='Set U')
        nx.draw_networkx_nodes(B, pos, nodelist=right_nodes, node_color='lightcoral', node_size=1000, label='Set O')
        nx.draw_networkx_edges(B, pos, width=1.0, alpha=0.5)
        nx.draw_networkx_labels(B, pos, font_size=10, font_color='black')

        # Agregámos título y leyendas
        plt.title("Gráfica Bipartita")
        plt.legend()
        plt.axis('off') # Hide axes

        # Visualizamos
        plt.show()

    visualiza_grafica_bipartita(B)
    return (visualiza_grafica_bipartita,)


@app.cell
def _(left_nodes, right_nodes):
    # Renombranos nombres de los nodos

    # Definimos un diccionario para renombrar los nombres de los nodos del conjunto U, conjunto 'bipartite=0'
    mapping_setU = {u : f"User-{u+1}" for u in left_nodes}

    # Definimos un diccionario para renombrar los nombres de los nodos del conjunto O, conjunto 'bipartite=1'
    mapping_setO = {o : f"Object-{o-len(left_nodes) + 1}" for o in right_nodes}

    # Combinamos los diccionarios
    combined_mapping = {**mapping_setU, **mapping_setO}
    combined_mapping
    return (combined_mapping,)


@app.cell
def _(B, combined_mapping, nx, visualiza_grafica_bipartita):
    # Relabel the nodes
    B_renamed = nx.relabel_nodes(B, combined_mapping, copy=True)
    visualiza_grafica_bipartita(B_renamed)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Construct the $N \times N$ matrix $B=A A^{\top}$ that describes the projection on the first set of nodes. What is the meaning of the off-diagonal terms and that of the diagonal terms in such a matrix?""")
    return


@app.cell
def _(A_nv):
    B_proyeccion_U = A_nv @ A_nv.T
    B_proyeccion_U
    return (B_proyeccion_U,)


@app.cell
def _(B_proyeccion_U, np):
    ## Eliminamos "rizos" (self loop edges)
    np.fill_diagonal(B_proyeccion_U, 0)
    B_proyeccion_U
    return


@app.cell
def _(B_proyeccion_U, left_nodes, nx, plt):
    # Creamos la gráfica dirigida a partir de la proyección de AA'
    G_proyeccion = nx.from_numpy_array(B_proyeccion_U, create_using=nx.Graph)

    # Definimos un diccionario para renombrar los nombres de los nodos del conjunto U, conjunto 'bipartite=0'
    mapping_setU_min = {u : f"U{u+1}" for u in left_nodes}

    G_proyeccion = nx.relabel_nodes(G_proyeccion, mapping_setU_min, copy=True)


    # Visualizamos la gráfica
    elarge = [(u, v) for (u, v, d) in G_proyeccion.edges(data=True) if d["weight"] > 1]
    esmall = [(u, v) for (u, v, d) in G_proyeccion.edges(data=True) if d["weight"] <= 1]

    pos = nx.spring_layout(G_proyeccion, seed=7)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G_proyeccion, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G_proyeccion, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(
        G_proyeccion, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(G_proyeccion, pos, font_size=15, font_family="sans-serif", font_color = "white")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G_proyeccion, "weight")
    nx.draw_networkx_edge_labels(G_proyeccion, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
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
def _(A_nv, np):
    similarity = (A_nv @ A_nv.T)/np.sum(A_nv, axis=1)[np.newaxis,:]
    similarity = np.maximum(similarity, similarity.T)
    similarity
    return (similarity,)


@app.cell
def _():
    return


@app.cell
def _(A_nv, np, similarity):
    recomendation_matrix = (np.dot(A_nv.T,similarity)/np.sum(similarity, axis=1)).T
    recomendation_matrix
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

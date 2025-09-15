// Get Polylux from the official package repository
#import "@preview/polylux:0.4.0": *
#import "@preview/pinit:0.2.2": *
#import "@preview/colorful-boxes:1.4.3":*
#import "@preview/thmbox:0.3.0": *
#import "@preview/mitex:0.2.5": *

//#show: thmbox-init()
// Make the paper dimensions fit for a presentation and the text larger
#let ukj-blue = rgb(0, 84, 163)


//#show link: underline

#let my-stroke = stroke(
  thickness: 2pt,
  paint: blue.lighten(50%),
  cap: "round",
)

#let new-section-slide(title) = slide[
  #set page(footer: none, header: none)
  #set align(horizon)
  #set text(size: 1.5em)
  #strong(title)
  #line(stroke: my-stroke, length: 50%)
  #toolbox.register-section(title)
]


#set page(paper: "presentation-16-9",
  margin: 5cm,
  footer: [
    #set text(size: .6em)
    #set align(horizon)
    Economía para el Desarrollo. Laboratorio 1
    //Andreas Kröpelin, January 2025 #h(1fr) #toolbox.slide-number
    #h(1fr) #box(image("images/tecnologico-de-monterrey-blue.png", height: 2em)) | #toolbox.slide-number
  ],
  header: box(stroke: (bottom: my-stroke), inset: 8pt)[
    #set text(size: .6em)
    #set align(horizon)
    #toolbox.current-section
    #h(1fr)
    //Polylux demo | #toolbox.current-section
    #box(image("images/lader.jpg", height: 4em))
  ]
)


#set text(size: 15pt, font: "Lato")
#set page(margin: 0.6in)

#show table.cell.where(y: 0): set text(weight: "bold")

#show figure: set block(breakable: true)

// Use #slide to create a slide and style it using your favourite Typst functions
#slide[
  #set align(horizon)
  = Redes Bipartitas y Sistemas de Recomendación

  Hermilo Cortés González

  July 23, 2023
]

#new-section-slide("Directed, Weighted and Bipartite Graphs")
#slide[
  
  #toolbox.side-by-side(gutter: 3mm, columns: (2fr, 2fr), 
  [
            #thmbox(
            variant: "Definition (Directed graph)", 
            color: orange,
            numbering : none,
            font: "Lato",
            fill: rgb("#fffdd3")
        )[
          #text(font: "Lato", size : 14pt)[
          #mitext(`
  A directed graph $G \equiv(\mathcal{N}, \mathcal{L})$ consists of two sets, $\mathcal{N} \neq \emptyset$ and $\mathcal{L}$. The elements of $\mathcal{N} \equiv\left\{n_1, n_2, \ldots, n_N\right\}$ are the nodes of the graph $G$. The elements of $\mathcal{L} \equiv\left\{l_1, l_2, \ldots, l_K\right\}$ are distinct ordered pairs of distinct elements of $\mathcal{N}$, and are called directed links, or arcs
  `)
          ]
        ]
            #example(
            variant: "Example. Airport shuttle",
            numbering : none,
            font: "Lato",
            )[
          #mitext(`
A large airport has six terminals, denoted by the letters $A, B, C, D, E$ and $F$. The terminals are connected by a shuttle, which runs in a circular path, $A \rightarrow B \rightarrow C \rightarrow D \rightarrow E \rightarrow F \rightarrow A$, as shown in the figure. Since $A$ and $D$ are the main terminals, there are other shuttles that connect directly $A$ with $D$, and vice versa. The network of connections among airport terminals can be properly described by a graph
  `)
            ]
  ], 

  [

      #figure(
        image("images/airport.png", width: 75%),
        numbering: none
      )
      #figure(
        image("images/airport_graph.png", width: 45%),
        numbering: none
      )
  ]
  )
]

#slide[
  
  #toolbox.side-by-side(gutter: 3mm, columns: (2fr, 2fr), 

  [
      #figure(
        image("images/airport_graph.png", width: 70%),
        numbering: none
      )
  ], 
        thmbox(
          variant: "", 
          title: "", 
          color: ukj-blue,
          numbering : none,
          font: "Lato"
      )[
          #text(font: "Lato", size : 13pt)[
            - $N=6$ nodes represent the terminals.
            - The links indicate the presence of a shuttle connecting one terminal to another.
            - In this case #text(fill: ukj-blue)[*it is necessary to associate a direction with each link*].
            - A #text(fill: ukj-blue)[*directed link*] is usually called an  #text(fill: ukj-blue)[*arc*].
            - The Graph has indeed K = 8 arcs.
            - Notice that there can be two arcs between the same pair of nodes. For instance, arc $(A, D)$ is different from arc $(D, A)$.
            - In a directed graph, an arc between node $i$ and node $j$ is denoted by the ordered pair $(i, j)$, and we say that the link is  #text(fill: ukj-blue)[*ingoing*] in $j$ and  #text(fill: ukj-blue)[*outgoing*] from $i$. 
            - Such an arc may still be denoted as $l_(i j)$.
            - However, at variance with undirected graphs, this time #text(fill: ukj-blue)[*the order of the two nodes is important*].    
            - #mitext(`
Namely, $l_{i j} \equiv(i, j)$ stands for an arc from $i$ to $j$, and $l_{i j} \neq l_{j i}$, or in other terms the arc $(i, j)$ is different from the arc $(j, i)$.
  `)        
          ]

      ]

  )
]

#slide[
        #text(font: "Lato", size : 15pt)[
          - The most basic definition is that of #text(fill: ukj-blue)[*undirected graph*], which describes systems in which  #text(fill: ukj-blue)[*the links have no directionality*]. 
          - In the case, instead, in which #text(fill: ukj-blue)[*the directionality of the connections is important, the directed graph definition is more appropriate*].
          - Also, we often need to deal with networks displaying a #text(fill: ukj-blue)[*large heterogeneity in the relevance of the connections*]. 
          - Typical examples are social systems where it is possible to measure the strength of the interactions between individuals.
        ]

        #figure(
        image("images/graphs.png", width: 85%),
        numbering: none
      )

]

#new-section-slide("Bipartite Graphs")

#slide[


  #toolbox.side-by-side(gutter: 3mm, columns: (2fr, 2fr), 
  [

      #text(font : "Lato", size : 20pt)[
        #v(20pt)
        #text(fill: ukj-blue)[*Bipartite graph*] is a graph whose nodes can be divided into two disjoint sets, such that every edge connects a vertex in one set to a vertex in the other set, while there are no links connecting two nodes in the same set.
      ]

    #thmbox(
    variant: "Definition (Bipartite graph)", 
    color: orange,
    numbering : none,
    font: "Lato",
    fill: rgb("#fffdd3")
        )[
          #text(font: "Lato", size : 14pt)[
          #mitext(`
        A bipartite graph, $G \equiv(\mathcal{N}, \mathcal{V}, \mathcal{L})$, consists of three sets, $\mathcal{N} \neq \emptyset, \mathcal{V} \neq \emptyset$ and $\mathcal{L}$. The elements of $\mathcal{N} \equiv\left\{n_1, n_2, \ldots, n_N\right\}$ and $\mathcal{V} \equiv\left\{v_1, v_2, \ldots, v_V\right\}$ are distinct and are called the nodes of the bipartite graph. The elements of $\mathcal{L} \equiv \left\{l_1, l_2, \ldots, l_K\right\}$ are distinct unordered pairs of elements, one from $\mathcal{N}$ and one from $\mathcal{V}$, and are called links or edges.
          `)
          ]
        ]
  ], 

  [
    #v(20pt)
    #figure(
        image("images/bipartita_paises.png", width: 64%),
        numbering: none
      )
      
  ]
  )
]

#slide[

  #text(font: "Lato", size : 17pt)[
  #v(10pt)
  - Many real systems are naturally bipartite. For instance, typical bipartite networks are #text(fill: ukj-blue)[*systems of users purchasing items such as books, or watching movies*]. 
  - An example is shown in the next figure, where we have denoted the user-set as #text(fill: ukj-blue)[$U = {u_1, u_2, dots, u_N}$] and the object-set as #text(fill: ukj-blue)[$O = {o_1, o_2, dots, o_V}$] 
  - In such a case we have indeed only  #text(fill: ukj-blue)[*links between users and items, where a link indicates that the user has chosen that item*].
  ]

    #figure(
        image("images/biapartita.png", width: 67%),
        numbering: none
      )
      
]

#slide[

  #text(font: "Lato", size : 16pt)[
  - Starting from a bipartite network, we can derive at least two other graphs. 
  - The first graph is #text(fill: ukj-blue)[*a projection of the bipartite graph on the first set of nodes*]: the nodes are the users and two users are linked if they have at least one object in common.
  - We can also assign a weight to the link #text(fill: ukj-blue)[*equal to the number of objects in common*].
  - The weight can be interpreted as a #text(fill: red)[*similarity between the two users*].
  ]

    #figure(
        image("images/proyeccion.png", width: 79%),
        numbering: none
      )
]

#new-section-slide("Recommendation Systems")
#slide[

  #text(font: "Lato", size : 16pt)[
  - Consider a system of users buying books or selecting other items, similar to the Figure
    #figure(
        image("images/biapartita.png", width: 60%),
        numbering: none
      )
  - Based on this, it is possible to construct #text(fill: red)[*recommendation systems*], i.e. to predict the user’s opinion on those objects not yet collected, and eventually to recommend some of them.
  - The simplest recommendation system, known as #text(fill: ukj-blue)[*global ranking method (GRM)*], sorts all the objects in descending order of degree and recommends those with the highest degrees.
  - Such a recommendation is based on the assumption that the most-selected items are the most interesting for the #text(fill: ukj-blue)[*average user*].
  - A more reﬁned recommendation algorithm, known as #text(fill: red)[*collaborative ﬁltering (CF)*], is based on similarities between users
  ]
  
]


#new-section-slide("How to Represent a Graph")

#slide[
  #text(font : "Lato", size : 16pt)[
    - There are different ways to completely describe a graph #mitext(`$G = (\mathcal{N}, \mathcal{L})$`) with $N$ nodes and $K$ links by means of a matrix. 
    - One possibility is to use the so-called #text(fill: ukj-blue)[*adjacency matrix*] $A$.
    #thmbox(
    variant: "Definition (Adjacency matrix)", 
    color: orange,
    numbering : none,
    font: "Lato",
    fill: rgb("#fffdd3")
        )[
          #text(font: "Lato", size : 14pt)[
          #mitext(`
        The adjacency matrix $A$ of a graph is a $N \times N$ square matrix whose entries $a_{i j}$ are either ones or zeros according to the following rule:

          $$
          a_{i j}=\left\{\begin{array}{c}
          1 \quad \text { iff }(i, j) \in \mathcal{L} \\
          0 \quad \text { otherwise }
          \end{array}\right.
          $$
          `)
          ]
        ]
    - In practice, for an undirected graph, entries $a_(i j)$ and $a_(j i)$ are set equal to 1 if there exists the edge $(i, j)$, while they are zero otherwise.
    - Thus, in this case, the adjacency matrix is symmetric.
    - If instead the graph is directed, $a_(i j)=1$ if there exists an arc from $i$ to $j$.
    - Notice that in both cases it is common convention to set #mitext(`$a_{i i} =0, \forall i=1, \ldots, N$`).
  ]


]



#slide[
    #example(
            numbering : none,
            font: "Lato",
            )[

              Consider the two graphs in the figure below. The first graph is undirected  and has $K = 4$ links, while the second graph is directed and has $K = 7$ arcs.
         #figure(
        image("images/two_graphs.png", width: 40%),
        numbering: none
      )

      The adjacency matrices associated with the two graphs are respectively:

          #mitext(`
            \begin{equation}
            A_u=\left(\begin{array}{ccccc}
            0 & 1 & 0 & 0 & 1 \\
            1 & 0 & 1 & 0 & 1 \\
            0 & 1 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 \\
            1 & 1 & 0 & 0 & 0
            \end{array}\right), \quad A_d=\left(\begin{array}{ccccc}
            0 & 1 & 0 & 0 & 1 \\
            0 & 0 & 1 & 0 & 0 \\
            0 & 0 & 0 & 1 & 1 \\
            0 & 1 & 0 & 0 & 0 \\
            1 & 0 & 0 & 0 & 0
            \end{array}\right)
            \end{equation}
          `)
  ]
]



#slide[
    #example(
            numbering : none,
            font: "Lato",
            )[

  #toolbox.side-by-side(gutter: 3mm, columns: (2fr, 2fr), 
  [

    #text(font: "Lato", size : 25pt)[
          #mitext(`
            \begin{equation}
            A_u=\left(\begin{array}{ccccc}
            0 & 1 & 0 & 0 & 1 \\
            1 & 0 & 1 & 0 & 1 \\
            0 & 1 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 \\
            1 & 1 & 0 & 0 & 0
            \end{array}\right)
            \end{equation}
          `)
          #v(20pt)
          #mitext(`
            \begin{equation}
            A_d=\left(\begin{array}{ccccc}
            0 & 1 & 0 & 0 & 1 \\
            0 & 0 & 1 & 0 & 0 \\
            0 & 0 & 0 & 1 & 1 \\
            0 & 1 & 0 & 0 & 0 \\
            1 & 0 & 0 & 0 & 0
            \end{array}\right)
            \end{equation}
          `)
    ]
  ], 

  [
    - $A_u$ is symmetric and contains $2K$ non-zero entries.
    - The number of ones in row $i$, or equivalently in column $i$, is equal to the degree of vertex $i$.
    - The adjacency matrix of a directed graph is in general not symmetric. This is the case of $A_d$.
    - This matrix has $K$ elements different from zero, and the number of ones in row $i$ is equal to the number of outgoing links #mitext(`$k_i^{\text {out }}$, while the number of ones in column $i$ is equal to the number of ingoing links $k_i^{\text {in }}$`).
  ]
  )

  ]
]

#slide[
  #v(20pt)
  #text(font : "Lato", size : 16pt)[
    -  A #text(fill: ukj-blue)[*Bipartite Graph*] can be represent by means of a slightly different definition of the adjacency matrix than that given above, and which in general is not a square matrix.
    - It can be described by an $N times V$ adjacency matrix $A$, such that entry $a_(i alpha)$, with $i=1, dots, N$ and $alpha=1, dots, V$, is equal to 1 if node $i$ of the first set and node $alpha$ of the second set are connected, while it is 0 otherwise. 
    - Using this representation of a bipartite graph in terms of an adjacency matrix, we show in the next example #text(fill: ukj-blue)[*how to formally describe a commonly used method to recommend a set of objects to a set of users*].
  ]

]


#new-section-slide("Recommendation systems: collaborative filtering")

#slide[

#text(font : "Lato", size : 16pt)[
  - Consider a bipartite graph of users and objects such as that shown in Figure 1.8, in which the existence of the link between node $i$ and node $alpha$ denotes that user $u_i$ has selected object $o_alpha$.
  - A famous personalised recommendation system, known as #text(fill: ukj-blue)[*collaborative filtering*] (CF), is based on the construction of a $N times N$ #text(fill: red)[*user similarity matrix*] $S = {s_(i j)}$.
  - The similarity between two users $u_i$ and $u_j$ can be expressed in terms of the adjacency matrix of the graph as:

          #mitext(`
        \begin{equation}
        s_{i j}=\frac{\sum_{\alpha=1}^V a_{i \alpha} a_{j \alpha}}{\min \left\{k_{u_i}, k_{u_j}\right\}},
        \end{equation}
          `)
  - Where #mitext(`$k_{u_i}=\sum_{\alpha=1}^V a_{i \alpha}$`) is the degree of user $u_i$ i.e. the number of objects chosen by $u_i$[324].
  - Based on the similarity matrix $S$, we can then construct an $N times V$ #text(fill: red)[*recommendation matrix*] $R = {r_(i a)}$.
  - In fact, for any user–object pair $u_i$, $o_alpha$, if $u_i$ has not yet chosen $o_alpha$, i.e. if $alpha_(i alpha) = 0$, , we can define a recommendation score $r_(i alpha)$ measuring to what extent $u_i$ may like $o_alpha$, as :

          #mitext(`
        \begin{equation}
        r_{i \alpha}=\frac{\sum_{j=1, j \neq i}^N s_{i j} a_{j \alpha}}{\sum_{j=1, j \neq i}^N s_{i j}} .
        \end{equation}
          `)




]

]

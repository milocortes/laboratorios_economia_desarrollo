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

#new-section-slide("Overview")
#slide[
        #thmbox(
          variant: "Definition (Directed graph)", 
          color: orange,
          numbering : none,
          font: "Lato",
          fill: rgb("#fffdd3")
      )[
        #text(font: "Lato", size : 12pt)[
        #mitext(`
A directed graph $G \equiv(\mathcal{N}, \mathcal{L})$ consists of two sets, $\mathcal{N} \neq \emptyset$ and $\mathcal{L}$. The elements of $\mathcal{N} \equiv\left\{n_1, n_2, \ldots, n_N\right\}$ are the nodes of the graph $G$. The elements of $\mathcal{L} \equiv\left\{l_1, l_2, \ldots, l_K\right\}$ are distinct ordered pairs of distinct elements of $\mathcal{N}$, and are called directed links, or arcs
`)
        ]
      ]
]

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
  = Métricas de Complejidad

  Hermilo Cortés González

  2 de Octubre de 2025
]

#new-section-slide("Definiciones Básicas")

#slide[

  = Matriz Ubicación-Actividad

  #thmbox(
            variant: "Definición (Matriz Ubicación-Actividad)", 
            color: orange,
            numbering : none,
            font: "Lato",
            fill: rgb("#fffdd3")
        )[
          #text(font: "Lato", size : 14pt)[
            Las Matrices Ubicación-Actividad conectan $c$ ubicaciones con $p$ actividades.

            $X_(c p)$ = Volumen de actividad $p$ en la ubicación $c$.

            Donde el Volumen de actividad puede referirse a exportaciones, ventas, pagos a nómina, valor agregado, empleo o alguna otra cantidad.
          ]
        ]

  - Dado que las unidades de los tamaños de actividades no son facilmente comparables (por ejemplo, China y Uruguay), las matrices necesitan ser normalizadas en #text(fill: ukj-blue)[*Matrices de Especialización, $R$*].
]

#slide[
  == Matrices de Especialización, $R$

  #thmbox(
      variant: "Definición (Matriz de Especialización, R)", 
      color: orange,
      numbering : none,
      font: "Lato",
      fill: rgb("#fffdd3")
  )[
    #text(font: "Lato", size : 16pt)[
      - Una Matriz de Especialización, $R$, se define al dividir cada entrada de la matriz $X_(c p)$ por la suma de sus respectivas filas o columnas.

      - Está medida se le conoce como #text(fill: ukj-blue)[*cociente de ubicación*] o #text(fill: ukj-blue)[*Revealed Comparative Advantage, (RCA)*].

      - Definiendo la suma de la matriz completa como  $X = sum_(c p) X_(c p)$ y usando la notación de Einsten en la que índices omitidos indizan variables sumadas #footnote[Para cualquier matrix$A_(i j)$, $A_i = sum_j A_(i j)$], la Matriz de Especialización $R_(c p)$ es 

      $
        R_(c p) = (X_(c p) X)/(X_c X_p)
      $

      $R_(c p)$ es la razón entre el nivel observado, $X_(c p)$, y el nivel esperado, $(X_c X_p)/X$, de actividad económica en una ubicación. 

     - Ubicaciones con $R_(c p) > 1$ se consideran  #text(fill: ukj-blue)[*especializadas en la actividad $p$*].
    ]
  ]

]


#slide[
  == Matriz de Especialización Binaria, $M$
  #thmbox(
      variant: "Definición (Matriz de Especialización Binaria, M)", 
      color: orange,
      numbering : none,
      font: "Lato",
      fill: rgb("#fffdd3")
  )[

    Definimos la Matriz de Especialización Binaria, $M$, como 

    #mitext(`
  \begin{aligned}
  &M_{c p}=\left\{\begin{array}{lll}
  1 & \text { if } & R_{c p} \geq R^{\star} \\
  0 & \text { if } & R_{c p}<R^{\star}
  \end{array}\right.\\
    `)

donde $R^(star)=1$ cuando usamos $R$ y $R^(star)=0.25$ cuando usamos $R^("pop")$

  ]

- $M$ remueve el exceso de variación al enfocarse sólo en las presencias ($M_(c p) = 1$) y ausencias, ($M_(c p) = 0$), significantes. 
- La suma por filas y columnas de $M$ contabiliza el número de actividades presentes en una ubicación (#text(fill: ukj-blue)[*diversidad*]) y el número de ubicaciones donde la actividad está presente (#text(fill: ukj-blue)[*ubicuidad*]), respectivamente.
- Formalmente:
    #mitext(`
\begin{aligned}
& M_c=\sum_p M_{c p}=\text { diversidad } \\
& M_p=\sum_c M_{c p}=\text { ubicuidad }
\end{aligned}
    `)

]


#slide[
  #text(font: "Lato", size : 20pt)[
  == Matriz de Especialización Binaria, $M$
  - Una propiedad de estas matrices geográficas es que la #text(fill: ukj-blue)[*ubicuidad*] promedio de las actividades presentes en una ubicación tienden a correlacionarse de forma negativa con la #text(fill: ukj-blue)[*diversidad*] de la ubicación.
  - Este hecho está relacionado con la propiedad de las matrices conocida como #text(fill: red)[*nestedness*] y puede ser vista como evidencia que #text(fill: ukj-blue)[*el conocimiento más complejo*] se #text(fill: ukj-blue)[*difunde*] con más dificultad y, por lo tanto, sólo está disponible en unas pocas ubicaciones diferentes.
  ]
]

#new-section-slide("Relatedness")

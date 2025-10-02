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

#let pinit-highlight-equation-from(height: 2em, pos: bottom, fill: rgb(0, 180, 255), highlight-pins, point-pin, body) = {
  pinit-highlight(..highlight-pins, dy: -0.9em, fill: rgb(..fill.components().slice(0, -1), 40))
  pinit-point-from(
    fill: fill, pin-dx: 0em, pin-dy: if pos == bottom { 0.5em } else { -0.9em }, body-dx: 0pt, body-dy: if pos == bottom { -1.7em } else { -1.6em }, offset-dx: 0em, offset-dy: if pos == bottom { 0.8em + height } else { -0.6em - height },
    point-pin,
    rect(
      inset: 0.5em,
      stroke: (bottom: 0.12em + fill),
      {
        set text(fill: fill)
        body
      }
    )
  )
}

#set page(paper: "presentation-16-9",
  margin: 5cm,
  footer: [
    #set text(size: .6em)
    #set align(horizon)
    Economía para el Desarrollo. Laboratorio 2
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
  #text(font: "Lato", size : 20pt)[
  = Matriz Ubicación-Actividad

  #thmbox(
            variant: "Definición (Matriz Ubicación-Actividad)", 
            color: orange,
            numbering : none,
            font: "Lato",
            fill: rgb("#fffdd3")
        )[
          #text(font: "Lato", size : 18pt)[
            Las Matrices Ubicación-Actividad conectan $c$ ubicaciones con $p$ actividades.

            $X_(c p)$ = Volumen de actividad $p$ en la ubicación $c$.

            Donde el Volumen de actividad puede referirse a exportaciones, ventas, pagos a nómina, valor agregado, empleo o alguna otra cantidad.
          ]
        ]

  - Dado que las unidades de los tamaños de actividades no son facilmente comparables (por ejemplo, China y Uruguay), las matrices necesitan ser normalizadas en #text(fill: ukj-blue)[*Matrices de Especialización, $R$*].
  ]
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

      #mitex(
        `
        $\mathrm{RCA}_{c p}= \dfrac{X_{c p} X}{X_c X_p}  = \frac{x_{c p} / \Sigma_p x_{c p}}{\Sigma_c x_{c p} / \Sigma_c \Sigma_p x_{c p}}$
        `
      )

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

#slide[
  #text(font: "Lato", size : 20pt)[
  == Relatedness
  - #text(fill: ukj-blue)[*Relatedness*] mide la afinidad entre una ubicación y una actividad.
  - #text(fill: ukj-blue)[*Relatedness*] se considera como un predictor de cambios en la especialización en la relación #text(fill: ukj-blue)[*ubicación-actividad*]#footnote[Se espera que una buena medida de afinidad prediga cambios en los patrones de especialización].
  - La medida de #text(fill: ukj-blue)[*Relatedness*] es construida usando #text(fill: red)[*redes que conectan actividades similares*].
  - Formalmente, relatedness $omega_(c p)$ puede ser definido como un predictor de la matriz de especialización que satisface:
    
    #mitext(`
    $R_{c p}(t+\mathrm{d} t)=R_{c p}(t)+B \omega_{c p}(t)+\ldots$
    `)

    donde $B$ es un coeficiente positivo y significativo.
  - Hay muchas formas de medir el relatedness. Particularmente, se han hecho avances en lo que se conoce como #text(fill: ukj-blue)[*Relatedness Density*].
  ]
]

#slide[
  #text(font: "Lato", size : 24pt)[
  == Relatedness Density

  - #text(fill: ukj-blue)[*Relatedness Density*] mira al número de actividades similares presentes en una ubicación.
  - Para calcular esta medida, primero definimos una  #text(fill: ukj-blue)[*Proximidad*].
  - Las medidas de proximidad conectan #text(fill: orange)[*parejas de actividades*], $phi.alt_(p p)$, o #text(fill: orange)[*parejas de ubicaciones*], $phi.alt_(c c)$.


  #toolbox.side-by-side(gutter: 3mm, columns: (2fr, 2fr), 
  [
    #mitext(`
  \begin{aligned}
  &\phi_{p p^{\prime}} \rightarrow \left\{\begin{array}{lll}
  \text{Product Space} \\
  \text{Industry Space} \\
  \text{Technology Space} \\
  \end{array}\right.\\
    `)
  ], 

  [
    #mitext(`
  \begin{aligned}
  &\phi_{c c^{\prime}} \rightarrow \left\{\begin{array}{lll}
  \text{Country Space} \\
  \text{Producer Space} \\
  \end{array}\right.\\
    `)

  ]
  )
  ]
]


#slide[
  == Relatedness Density
        #figure(
      image("images/product_space.png", width: 100%),
      caption: [Tomado de @hidalgo2021economic.]
    ) 
]

#slide[
  == Relatedness Density
        #figure(
      image("images/otros_espacios.png", width: 100%),
      caption: [Tomado de @hidalgo2021economic.]
    ) 
]
#slide[
  
  #text(font: "Lato", size : 20pt)[
  == Relatedness Density

  - Hay múltiples formas de medir #text(fill: ukj-blue)[*Proximidad*]. Algunas, como la #text(fill: ukj-blue)[*probabilidad condicional mínima*], miran a la colocalización o coaglomeración de actividades:

  #mitex(
  `
  $\phi_{p p^{\prime}}=\frac{\sum_c M_{c p} M_{c p^{\prime}}}{\max \left(M_p, M_{p,}\right)}$
  `
  )

  - Otras utilizan la correlación entre filas y columnas de la matriz de especialización:
  
  #mitex(
    `
    $\phi_{c c^{\prime}}=\operatorname{corr}\left(\log \left(R_{c p}\right), \log \left(R_{c^{\prime} p}\right)\right)$
    `
  )

  - La proximidad también ha sido medida por los requerimientos de skills entre industrias.
  - Las redes de proximidad han sido construidas para una gran variedad de conjunto de datos revelando diferencias en los patrones de las redes.
  ]
]

#slide[
  #text(font: "Lato", size : 22pt)[
  == Relatedness Density
  - Con la medida de proximidad, podemos calcular #text(fill: ukj-blue)[*Relatedness Density*] como la fracción de actividades relacionadas presentes en una ubicación 

  #mitex(
    `
$\omega_{c p}=\frac{\sum_{p\prime} M_{c p\prime} \phi_{p p^{\prime}}}{\sum_{p,} \phi_{p p^{\prime}}}$ \quad \text{o} \quad $\omega_{c p}=\frac{\sum_{c \prime} M_{c \prime} \phi_{c \prime c}}{\sum_{c \prime} \phi_{c \prime c}}$
    
    `
  )
  - Algunas variaciones implican usar el cuadrado de las entradas de la matriz de proximidad #mitext(`$\phi_{p p^{\prime}}$`) para incrementar el peso de actividades más próximas. 
  - Alternativas para calcular relatedness:
    - Singular Value Decomposition, SVD.
    - Factores latentes para ubicaciones y actividades.
  ]

]

#new-section-slide("Economic Complexity")

#slide[
  == Economic Complexity
  - Las medidas de #text(fill: ukj-blue)[*Complejidad Económica*] miden la capacidad económica con #text(fill: ukj-blue)[*métodos de reducción de dimensionalidad*].
  - Representan también funciones de producción generalizadas de dimensionalidad reducida.
  - Las medidas de complejidad económica pueden ser utilizadas para medir la presencia de múltiples factores económicos en una forma que es #text(fill: red)[*agnóstica*] sobre cuales podrían ser esos factores.
  - Formalmente, la complejidad $K_c$ de una ubicación $c$ y la complejidad $K_p$ de una actividad $p$ puede definirse como una función una de la otra:
  #mitex(
    `
    $K_c=f\left(M_{c p}, K_p\right)$
    `
  )

  #mitex(
    `
    $K_p=g\left(M_{c p}, K_c\right)$
    `
  )

  - Estas ecuaciones declaran que la complejidad de una ubicación es una función de la complejidad de las actividades que están presentes en esta, y viceversa.
  - #text(fill: red)[*Una economía es tan compleja como las actividades que puede realizar, y una actividad es tan compleja como los lugares que pueden realizarla*].
]

#slide[
  == Economic Complexity

  - La idea de medir la complejidad usando estas ecuaciones acopladas fue introducida por Cesar Hidalgo y Ricardo Haussman @hidalgo2009building. Los autores utilizan promedios simples para $f$ y $g$.
  - Las medidas resultantes se conocen como #text(fill: ukj-blue)[*Índice de Complejidad Económica, (ECI; $K_c$)*] y el #text(fill: ukj-blue)[*Índice de Complejidad de Producto, (PCI; $K_p$)*].
  - Estas medidas están definidas por el siguiente sistema de ecuaciones:

  #mitex(
    `
    $K_c=\frac{1}{M_c} \sum_p M_{c p} K_p$
    `
  )

  #mitex(
    `
    $K_p=\frac{1}{M_p} \sum_c M_{c p} K_c$
    `
  )

  Reemplazando la segunda ecuación en la primera:

  #mitex(
    `
    $K_c=\widetilde{M}_{c c}, K_{c t}$
    `
  )

  donde 

  #mitex(
    `
    $\widetilde{M}_{c c \prime}=\sum_p \frac{M_{c p} M_{c \prime p}}{M_c M_p}$
    `
  )


]

#slide[
  == Economic Complexity

  - Originalmente el cálculo de ECI y PCI se definió mediante un método iterativo llamado  #text(fill: ukj-blue)[*algoritmo de reflexión*] que primero calcula la diversidad y ubicuidad para posteriormente y luego utiliza recursivamente la información de uno para corregir el otro.
  - Se puede demostrar @caldarelli2012network @cristelli2013measuring que el método de reflección es equivalente a encontrar los eigenvalores de la matriz $tilde(M)$#footnote[Cuyas filas y columnas corresponden a paises y productos, $i.e$ $tilde(M) = tilde(M)_(c c')$]

  #mitex(
    `
    $\tilde{M}=D^{-1} M U^{-1} M^{\prime}$
    `
  )
  donde $D$ es la matriz diagonal formada a partir del vector de diversidad y $U$ es la matriz diagonal formada a partir del vector de ubicuidad @mealy2019interpreting. 
  
  - En el contexto de datos de comercio entre países, podemos pensar a $tilde(M)$ como una matriz de diversidad-ponderada (o normalizada) que refleja qué tan similares son las canastas exportadoras de los dos países, es decir, que tan similares son sus patrones de especialización. 
]

#slide[
  == Economic Complexity
  - De la ecuación anterior podemos ver que:
  #mitex(
    `
    $\tilde{M}=D^{-1} S$
    `
  )

donde $S = M U^(-1) M^'$ es una matriz de similaridad simétrica en que cada elemento $S_(c c')$ representa los productos que el pais $c$ tiene en común con el país $c'$, ponderado o normalizado por la inversa de la ubicuidad de cada producto.

- Dado que $tilde(M)$ es una  #text(fill: ukj-blue)[*Matriz Estocástica*] (la suma de sus filas suman 1, $sum_c M_(c c') = 1$), sus entradas pueden ser interpretadas como probabilidades de transición condicionales de una #text(fill: ukj-blue)[*Matriz de Transición de Markov*].
- El ECI se define como el eigenvector asociado con el segundo eigenvalor más grande de $tilde(M)$#footnote[El eigenvector asociado con el primer eigenvalor más grande de una matriz estocástica es siempre un vector de unos].
- Este eigenvector determina una #text(fill: ukj-blue)[*Distancia de difusión*] o #text(fill: ukj-blue)[*Velocidad de Convergencia*] entre las probabilidades estacionarias de los estados alcanzados por un paseo aleatorio descrito por esta matriz de transición de Markov.
  
]


#slide[
#text(font: "Lato", size : 25pt)[
  == Economic Complexity

- En términos económicos, el #text(fill: red)[*ECI is el vector que mejor divide las economías en grupos basado en las actividades que están presentes en estas*].
- Economic complexity is intimately connected to SVD, a matrix factorization technique that provides the best way to explain the structure of a matrix
]
]

#slide[
#text(font: "Lato", size : 25pt)[
  == Product Complexity
  El PCI es simétricamente definido al transponer la matriz $M_(c p)$ y encontrando el eigenvector correspondiente al segundo eigenvalor más grande de la matriz $hat(M)$dada por 

  #mitex(
    `
    \begin{equation}
\hat{M}=U^{-1} M^{\prime} D^{-1} M
\end{equation}
    `
  )
]
]

#slide[
  #text(font: "Lato", size : 22pt)[
  == Economic Complexity
  - Las métricas de complejidad económica se suelen normalizar mediante una transformación $Z$ #footnote[Válido para estás medidas dado que no siguen una distribución de colas pesadas]:
  #mitex(
    `
    $\operatorname{ECI}_c=\left(K_c-\operatorname{mean}\left(K_c\right)\right) / \operatorname{stdev}\left(K_c\right)$,
    `
  ) 

  #mitex(
    `
    $\operatorname{PCI}_c=\left(K_p-\operatorname{mean}\left(K_p\right)\right) / \operatorname{stdev}\left(K_p\right)$,
    `
  ) 

  - Valores con un ECI $>0$ representan ubicaciones con una complejidad que es más grande que el promedio en el conjunto de datos analizado#footnote[La interpretación es similar al PCI].
]
]
#slide[
  == Wee need to do all these calculations to find the ECI connected to $Y_(c p)$
        #figure(
      image("images/eci_pipeline.jpeg", width: 85%),
      caption: [Tomado de https://x.com/cesifoti/status/1972294955868782680]
    ) 
]

#slide[
  == By why does it work in theory? Does it really estimate the availability of factors in an economy? If so, what factors? Any factors?

  #figure(
      image("images/theory_economic_complexity.png", width: 85%),
      caption: [https://arxiv.org/abs/2506.18829]
  ) 
]


#slide[
  == Usemos el hilo de César Hidalgo#footnote[https://x.com/cesifoti/status/1972294955868782680]
  - Consideremos que cada economía está dotada de factores que sus actividades requieren.
  - En ese mundo, la producción potencial de una economía en una actividad es la probabilidad de que esté dotada de los factores requeridos por esa actividad.
  - En un modelo dónde solo hay *una* capacidad, escribir esa producción uno menos la probabilidad que esa economía no tenga la capacidad que el producto requiere#footnote[Esta formulación corresponde a la función de activación ReLU con parámetro $q=1$] : 


#v(5em)



#text(font: "Lato", size : 20pt)[$ Y_(c p) = A (1- #pin(1)q_p#pin(2) #pin(3) (1-r_c) #pin(4)) $]

#pinit-highlight-equation-from((1,2), (1, 2), height: 3.5em, pos: bottom, fill: rgb(0, 180, 255))[
  Probabilidad que la actividad $p$ requiera la capacidad
]

#pinit-highlight-equation-from((3, 4), (3, 4), height: 2.5em, pos: top, fill: rgb(150, 90, 170))[
  Probabilidad que la economía $c$ carezca de la capacidad
]

]
#slide[

  == Para $N_b$ capacidades
  - Para un número arbitrario de factores, la fórmula se generaliza a :
#v(5em)

#text(font: "Lato", size : 20pt)[$ #pin(5) Y_(c p) #pin(6) = A product_(b=1)^(N_b)  (1- #pin(7)q_(p,b)#pin(8) #pin(9) (1-r_(c,b)) #pin(10)) $]

#pinit-highlight-equation-from((5,6), (5, 6), height: 3.5em, pos: bottom, fill: rgb(255, 69, 0))[
  Output
]

#pinit-highlight-equation-from((7,8), (7, 8), height: 3.5em, pos: bottom, fill: rgb(0, 180, 255))[
  Prob que la actividad $p$ requiera la capacidad $b$
]

#pinit-highlight-equation-from((9, 10), (9, 10), height: 2.5em, pos: top, fill: rgb(150, 90, 170))[
  Prob que la economía $c$ carezca la capacidad $b$
]
]

#slide[
  == ¿Podemos recuperar la matriz de dotación de factores $r$ sí solo observamos la matriz de salida $Y$?

  - #text(fill: ukj-blue)[*SÍ*].
  - #text(fill: red)[*La Complejidad Económica es un estimador monótono de las dotaciones de factores que es robusto a las variaciones en tamaño y ruido*].
  - Para un factor, no es dificil calcular la matriz $M_(c c')$ asociada a esta función de producción. 
  - Esta matriz separa las economías con una probabilidad superior al promedio de tener un factor de aquellas con una probabilidad inferior al promedio.
  ]


#slide[
  == La forma de la matriz es simple cuando el número de economías y actividades es par 
#text(font: "Lato", size : 26pt)[
  #v(1cm)

  #mitex(
    `
    \begin{equation}
M_{c c^{\prime}}=\frac{1}{M_c} \sum_p \frac{M_{c p} M_{c^{\prime} p}}{M_p}
\end{equation}
    `
  )

    #mitext(`
  \begin{aligned}
  &M_{c c^{\prime}}=\left\{\begin{array}{lll}
  \frac{1}{M_p} & \text { if }  \quad r_c \& r_{c^{\prime}} \geq\langle r\rangle \quad \& \quad r_c \& r_{c^{\prime}}<\langle r\rangle\\
  0 & \text { Otherwise}
  \end{array}\right.\\
    `)


  #mitex(`
$$
M_{c p}=\left[\begin{array}{llllll}
0 & 0 & 0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 & 1 & 1 \\
1 & 1 & 1 & 0 & 0 & 0 \\
1 & 1 & 1 & 0 & 0 & 0
\end{array}\right] \quad \rightarrow \quad M_{c c^{\prime}}=\left[\begin{array}{cccc}
1 / 2 & 1 / 2 & 0 & 0 \\
1 / 2 & 1 / 2 & 0 & 0 \\
0 & 0 & 1 / 2 & 1 / 2 \\
0 & 0 & 1 / 2 & 1 / 2
\end{array}\right]
$$
  `)
]
]


#slide[
  == Se vuelve más complicado cuando son impares, pero el resultado es el mismo
#text(font: "Lato", size : 18pt)[

  #v(0.5cm)
  #mitex(
    `
  \begin{equation}
  M_{c p}=\left[\begin{array}{lll|l|lll}
  0 & 0 & 0 & 1 & 1 & 1 & 1 \\
  0 & 0 & 0 & 1 & 1 & 1 & 1 \\
  \hline 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
  \hline 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
  1 & 1 & 1 & 1 & 0 & 0 & 0
  \end{array}\right] \quad \rightarrow \quad M_{c c^{\prime}}=\left[\begin{array}{ccccc}
  3 / 10 & 3 / 10 & 3 / 10 & 1 / 20 & 1 / 20 \\
  3 / 10 & 3 / 10 & 3 / 10 & 1 / 20 & 1 / 20 \\
  6 / 35 & 6 / 35 & 11 / 35 & 6 / 35 & 6 / 35 \\
  1 / 20 & 1 / 20 & 3 / 10 & 3 / 10 & 3 / 10 \\
  1 / 20 & 1 / 20 & 3 / 10 & 3 / 10 & 3 / 10
  \end{array}\right]
  \end{equation}
    `
  )
  #v(0.7cm)

  #mitext(`
  \begin{aligned}
  &M_{c c^{\prime}}=\left\{\begin{array}{lll}
  \frac{1}{M_c}\left(1+\frac{1}{N_p}\right) \quad \text { if } \quad r_c \& r_{c^{\prime}}>\langle r\rangle \quad \text { or } \quad r_c \& r_{c^{\prime}}<\langle r\rangle \\
  \\
  \frac{1}{M_c}\left(\frac{1}{N_p}\right) \quad \text { if } \quad r_c>\langle r\rangle \quad \& \quad r_{c^{\prime}}<\langle r\rangle \text { and vice versa }\\
  \\
  \frac{1}{N_c}\left(\frac{1}{N_p}+\frac{N_c-1}{M_p}\right) \quad \text { if } \quad c=c^{\prime} \quad \& \quad r_c=\langle r\rangle\\
  \\
  \frac{1}{N_c}\left(1+\frac{1}{N_p}\right) \quad \text { if } \quad c \neq c^{\prime} \quad \& \quad \text { if } \quad r_c=\langle r\rangle \\
  \\
 \frac{1}{M_c}\left(1+\frac{1}{N_p}\right) \quad \text { if } \quad r_{c^{\prime}}=\langle r\rangle
  \end{array}\right.\\
  `)

]
]



#slide[
  == El segundo eigenvector de esta matriz indica a qué grupo pertenece una economía. Estimamos los factores económicos sin tener que definirlos#footnote[Esta es una propiedad de agrupamiento espectral del segundo vector propio de una matriz. Se ha mostrado que matemáticamente el ECI es equivalente al método de agrupamiento espectral para particionar un gráfica pesada y no dirigida $S$, en dos componentes balanceados @mealy2019interpreting. La técnica de agrupamiento espectral es ampliamente usada para tareas de detección de comunidades y reducción de dimensionalidad teniendo un rango amplio de aplicaciones como reconocimiento de imágenes, rankeo de páginas web, clasificación de motif de RNA, etc.].
#text(font: "Lato", size : 19pt)[
  #v(1cm)

  #mitex(
    `
    \begin{equation}
M_{c c^{\prime}}=\left[\begin{array}{ccccc}
3 / 10 & 3 / 10 & 3 / 10 & 1 / 20 & 1 / 20 \\
3 / 10 & 3 / 10 & 3 / 10 & 1 / 20 & 1 / 20 \\
6 / 35 & 6 / 35 & 11 / 35 & 6 / 35 & 6 / 35 \\
1 / 20 & 1 / 20 & 3 / 10 & 3 / 10 & 3 / 10 \\
1 / 20 & 1 / 20 & 3 / 10 & 3 / 10 & 3 / 10
\end{array}\right] \quad e_c^2=E C I_c=\left[\begin{array}{c}
a \\
a \\
0 \\
-a \\
-a
\end{array}\right]
\end{equation}
    `
  )
  #v(1cm)

  #mitex(
    `
    \begin{equation}
\begin{array}{lll}
e_c^2=E C I_c=a & \text { if } & r_c>\langle r\rangle \\
e_c^2=E C I_c=-a & \text { if } & r_c<\langle r\rangle \\
e_c^2=E C I_c=0 & \text { if } & r_c=\langle r\rangle
\end{array}
\end{equation}
    ` 
  )
]
]




#slide[
  == Interpreting the ECI as a spectral clustering method @mealy2019interpreting

        #figure(
      image("images/aau1705-f1.jpeg", width: 85%),
      caption: text(font: "Lato", size : 9pt)[Tomado de Mealy(2019). Each panel shows the ECI vector (in ascending order) (left) and the associated similarity matrix S (right), where rows and columns have been ordered by the ECI and colored by the Sij values. Panels correspond to similarity networks based on (A) randomly generated data with two clear components, (B) HS6 COMTRADE data for 2013, (C) data on employment concentrations in different industries in U.K. local authorities (LAs), and (D) data on employment concentrations in different occupations in U.S. states.]
    ) 
]

#slide[
  == Resultados de agrupación para datos random 
          #figure(
      image("images/murphy_spectral_clustering.png", width: 85%),
      caption: [a) K-means, b) Spectral Clustering. Tomado de @murphy2022probabilistic]
    ) 
]

#slide[
  == ¿Cómo se mueven los países a través del espacio producto? Desarrollando productos cercanos a aquellos que actualmente ya producen @hausmann2014atlas
  - La Proximidad mide la similaridad entre pares de actividades-productos.
  - Necesitamos una medida que cuantifique la #text(fill: ukj-blue)[*Distancia*] entre las actividades especializadas en un país y las actividades donde no está especializada.

  #mitex(
    `
$d_{c p}=\frac{\sum_{p'} (1 - M_{c p'}) \phi_{p p^{\prime}}}{\sum_{p,} \phi_{p p^{\prime}}}$ 
    
    `
  )

  - La distancia nos da una idea de qué tan lejos está cada actividad dado el ecosistema productivo del país.
  - Sería útil tener una medida holística de las oportunidades que implica la posición de un país en el espacio de productos.
  - Es razonable #text(fill: ukj-blue)[*incluir no sólo la distancia a las actividades, sino también su complejidad*].
]

#slide[
  == Algunos países pueden estar ubicados cerca de pocos productos, mal conectados y relativamente simples. 
        #figure(
      image("images/nigeria_ps.png", width: 85%),
      caption: [Product Space Nigeria 2023. Tomado del Atlas de Complejidad Económica]
    ) 
]

#slide[
  == Mientras que otros pueden tener un rico vecindario sin explotar de productos altamente conectados o complejos. 
        #figure(
      image("images/mexico_ps.png", width: 85%),
      caption: [Product Space México 2023. Tomado del Atlas de Complejidad Económica]
    ) 
]

#slide[
  == Opportunity Value - Economic Complexity Outlook Index (COI)
  - Los lugares difieren no sólo en lo que se especializan o producen, sino también en sus oportunidades.
  - Este #text(fill: ukj-blue)[*opportunity value*] de opciones explotadas se cuantifica al agregar el nivel de complejidad de las actividades que actualmente no están especializadas, ponderado por cuán cerca están estos productos del ecosistema productivo actual del lugar.
  #mitex(
    `
    $$
\text { opportunity value }_c=\sum_{p^{\prime}}\left(1-d_{c p^{\prime}}\right)\left(1-M_{c p^{\prime}}\right) P C I_{p^{\prime}}
$$ `
  )
  - El término $1 - M_(c p')$ se asegura de contabilizar solo actividades no especializadas.
  - Un valor alto del opportunity value implica estar en la proximidad de más actividades y/o de actividades más complejas.

]

#slide[
  == Opportunity Gain - Opportunity Outlook Gain (COG)
  - Podemos utilizar el opportunity value para calcular el beneficio potencial que obtendría un lugar si se especializa en una nueva actividad particular.
  - Se llama a este valor como la #text(fill: ukj-blue)[*ganancia de oportunidad (Opportunity Gain)*] que un lugar $c$ obtendría de especializarse en la actividad $p$.
  - Se calcula como el cambio en el valor de oportunidad obtenido de especializarse en la actividad $p$.
  - La ganancia de oportunidad cuantifica la contribución de especializarse en una nueva actividad en términos de abrir las puertas a actividades cada vez más complejas.
  - Formalmente la calculamos como#footnote[
    En la publicación *The atlas of economic complexity: Mapping paths to prosperity* se especifica la siguiente fórmula para el Opportunity Gain
      #mitex(
    `
    \begin{equation}
\text { opportunity gain }_c=\sum_{p^{\prime}} \frac{\phi_{p p^{\prime}}}{\sum_{p^{\prime \prime}} \phi_{p^{\prime \prime} p^{\prime}}}\left(1-M_{c p^{\prime}}\right) P C I_{p^{\prime}}-\left(1-d_{c p}\right) P C I_p
\end{equation}
    `
  )

  Aquí usaremos la especificación del glosario del portal del Atlas de Complejidad Económica (https://atlas.hks.harvard.edu/glossary)
  ]:

  #mitex(
    `
    \begin{equation}
\text { opportunity gain }_c=\sum_{p^{\prime}} \frac{\phi_{p p^{\prime}}}{\sum_{p^{\prime \prime}} \phi_{p^{\prime \prime} p^{\prime}}}\left(1-M_{c p^{\prime}}\right) P C I_{p^{\prime}}
\end{equation}
    `
  )
]

#slide[
  #bibliography("references.bib",  style: "apa")
]


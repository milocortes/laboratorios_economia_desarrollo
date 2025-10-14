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
    Economía para el Desarrollo. Laboratorio 3
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
  = Identificación de Oportunidades de Diversificación

  Hermilo Cortés González

  18 Septiembre 2024
]

#new-section-slide("The policy implications of economic complexity")
#slide[
  = The policy implications of economic complexity @HIDALGO2023104863

    #figure(
      image("images/hidalgo_2023.png", width: 85%),
    ) 
]
#new-section-slide("What")
#slide[
  == What
  - Se enfoca en identificar:
    - Actividades en las que las ubicaciones podrían diversificarse o 
    - Ubicaciones más adecuadas para el desarrollo de una actividad.
  - Estos enfoques usan #text(fill: red)[*métricas de relatedness*] para #text(fill: ukj-blue)[*recomendar las actividades en las que una economía debería enfocarse*] así como #text(fill: red)[*métricas de complejidad*] para evaluar #text(fill: ukj-blue)[*el valor potencial de la especialización*].
  - También se incluyen otrás métricas objetivo que el valor potencial como las intensidades de emisiones de CO2 o la desigualdad asociada con la actividad.
  - Usualmente la forma como se implementa este enfoque es mediante #text(fill: ukj-blue)[*diagramas relatedness-complexity*]#footnote[Introducidos inicialmente en el Atlas de Complejidad Económica @hausmann2014atlas]
  - Para una economía (e.g. un país, ciudad o región), el diagrama relatedness-complexity grafica el relatedness (o distancia) entre esa ubicación y cada actividad en el eje-$x$ y la complejidad (o alguna otra métrica de valor) de cada actividad en el eje-$y$.

]


#slide[
    == Exportaciones de Shanghai,indica las oportunidades potenciales de exportación. 
        #figure(
      image("images/relatedness_complexity_diag_pais.png", width: 75%),
      caption: [Tomado @HIDALGO2023104863]
    ) 
]

#slide[
    == Similar para actividades, se grafican las ubicaciones que están más relacionadas a una actividad y la complejidad de cada ubicación.
        #figure(
      image("images/relatedness_complexity_diag_producto.png", width: 75%),
      caption: [Tomado @HIDALGO2023104863]
    ) 
]

#slide[
  == Podemos pensar los diagramas relatedness-complexity en término de 4 cuadrantes

    #figure(
      image("images/cuadrantes.png", width: 79%),
      caption: [Tomado @HIDALGO2023104863]
    ) 

]

#slide[
  == Podemos pensar los diagramas relatedness-complexity en término de 4 cuadrantes

  #toolbox.side-by-side(gutter: 3mm, columns: (3fr, 2fr), 
  [
    #figure(
      image("images/cuadrantes.png", width: 95%),
      caption: [Tomado @HIDALGO2023104863]
    ) 
  ],
  [
    #colorbox(
      title: [*Let it be*],
      color: "blue",
      radius: 2pt,
      width: auto,
    )[
      Muestra actividades que son tanto *deseables* (alta complejidad)#footnote[Se utilizan también otras medidas de deseabilidad, como las emisiones, tamaño de mercado, uso de agua, nivel esperado de desigualdad, etc.] y *accesibles* (alto relatedness).

      En este cuadrante la diversificación es factible y deseable.
    ]
  ]
  )

]

#slide[
  == Podemos pensar los diagramas relatedness-complexity en término de 4 cuadrantes

  #toolbox.side-by-side(gutter: 3mm, columns: (3fr, 2fr), 
  [
    #figure(
      image("images/cuadrantes.png", width: 95%),
      caption: [Tomado @HIDALGO2023104863]
    ) 
  ],
  [
    #colorbox(
      title: [*Wish you were here*],
      color: "blue",
      radius: 2pt,
      width: auto,
    )[
      Muestra actividades que son deseables pero menos accesibles.

      La diversificación en estas actividades es deseable pero difícil.
    ]
  ]
  )
]

#slide[
  == Podemos pensar los diagramas relatedness-complexity en término de 4 cuadrantes

  #toolbox.side-by-side(gutter: 3mm, columns: (3fr, 2fr), 
  [
    #figure(
      image("images/cuadrantes.png", width: 95%),
      caption: [Tomado @HIDALGO2023104863]
    ) 
  ],
  [
    #colorbox(
      title: [*Long road ahead*],
      color: "blue",
      radius: 2pt,
      width: auto,
    )[
      Muestra actividades que son accesibles pero poco atractivas.  

      La diversificación es factible, pero no son demasiado atractivas en términos de complejidad.
    ]
  ]
  )
]

#slide[
    == La mayoría de los productos que Shanghai exporta con ventaja comparativa están en el cuadrante alta complejidad-alto relatedness.  
    #figure(
      image("images/relatedness_complexity_diag_pais.png", width: 75%),
    ) 
]

#slide[
    == Para actividades, el diagrama puede usarse para recomendar ubicaciones que son adecuadas para una actividad. China y Turquía son países con alto potencial de desarrollar ventajas comparativas en motores de encendido por chispa.
        #figure(
      image("images/relatedness_complexity_diag_producto.png", width: 75%),
      caption: [Tomado @HIDALGO2023104863]
    ) 
]

#slide[
  == Los diagramas Relatedness-Complejidad son una herramienta exploratoria que puede ser usada para identificar oportunidades de diversificación que son tanto factibles (alto relatedness) y atractivas (alta complejidad).

  Los diagramas pueden ser modificados para elegir :
  
  - #text(fill: ukj-blue)[*Distintas medidas de relatedness*]:

    - Podemos utilizar un modelo que involucre varios predictores para obtener una medida de la ventaja comparativa implícita.
    - Usar enfoques de aprendizaje de máquina para estimar la probabilidad de diversificación.

  - #text(fill: ukj-blue)[*Distintas medidas de complejidad* o valor económico]:
    - Tamaño de mercado actual de la actividad.
    - Crecimiento de mercado de la actividad.
    - Emisiones de CO2 de la actividad (Green diversification).

  Dichas extensiones no cambian la idea básica detrás del enfoque: #text(fill: red)[*identificar actividades de mejora potencial que sean viables y atractivas*].
]

#slide[
  == Correlación negativa entre PCI y el relatedness para diferentes niveles de complejidad económica. A niveles relativamente bajos de complejidad (e.g. ECI < 0), las economías exhiben una correlación negativa entre relatedness y complejidad. Esas economías están relacionadas con actividades de baja complejidad.
    #figure(
      image("images/reversal_correlation.png", width: 110%),
    ) 
]

#slide[

  - Para economías poco complejas, las actividades más factibles no son atractivas (baja complejidad) mientras que las actividades más atractivas (alta complejidad) son difíciles de desarrollar (bajo relatedness).
  - Economías más complejas están en una posición estratégica más favorable :  las actividades más atractivas son también las más factibles.
  - La correlación negativa entre relatedness y complejidad ha sido propuesto como una explicación para trampas de ingreso medio, ya que es un patrón que diferencia entre economías de ingresos medios de alta y baja complejidad.
]

#new-section-slide("When")

#slide[
  = #text(fill: ukj-blue)[*Cuándo*] debe una economía entrar en actividades relacionadas o no relacionadas?#footnote[Related y unrelated.]

  - ¿Cómo debería cambiar este cálculo a medida que una economía asciende en la escala de complejidad?
  - Los enfoques del #text(fill: ukj-blue)[*Qué*] se enfocan en identificar actividades objetivo.
  - Los enfoques del #text(fill: ukj-blue)[*Cuándo*] nos indican cuándo enfocarnos en actividades relacionadas y no relacionadas.
  - #text(fill: ukj-blue)[*¿Cuál es la estrategia óptima para diversificar una economía?*] @alshamsi2018optimal
  - Efecto de segundo orden : qué caminos puede abrir la diversificación? 
  - Alshamsi et al (2018) muestran que las #text(fill: ukj-blue)[*estrategias que se enfocan puramente en el relatedness*] (dirigiendo la estrategia de diversificación a actividad más relacionadas) #text(fill: ukj-blue)[*son estrategias subóptimas de diversificación*].
  - Una mejor estrategia es la que se enfoca en un #text(fill: ukj-blue)[*portafolio*] de actividades (relacionadas o no relacionadas).
  - En este enfoque de portafolio, las estrategias buscan #text(fill: ukj-blue)[*equilibrar los esfuerzos*] para ingresar a actividades relacionadas y no relacionadas.
  - Actualmente las estrategias del #text(fill: ukj-blue)[*Qué*] dominan el uso actual de los métodos de complejidad en policy, pero las estrategias #text(fill: ukj-blue)[*Cuándo*] podrían ser la clave para economías estancadas en trampas de ingreso medio.
 
]


#slide[
  == The ECI optimization method presented in this paper provides a solution for the portfolio problem by identifying a combination of related and unrelated diversification targets that match the behavior expected in an optimal portfolio. @stojkoski2025optimizingeconomiccomplexity


    #figure(
      image("images/optimizing_eci.png", width: 70%),
    ) 
]

#slide[
  ==  Durante la última década, varios esfuerzos orientados a políticas han intentado expandir o mejorar el uso de los diagramas de relatedness-complejidad @stojkoski2025optimizingeconomiccomplexity


  Algunos reportes de desarrollo para paises agregan extensiones a los diagramas relatedness-complejidad

  - #text(fill: ukj-blue)[*Rwanda*] @hausmann2015moving : se identificaron objetivos de diversificación de exportaciones usando diagramas de relatedness-complejidad para posteriormente filtrarlos usando #text(fill: ukj-blue)[*criterios adicionales*] como el costo de transporte.
  - #text(fill: ukj-blue)[*Panamá*] @hausmann2017appraising: el criterio adicional fue la migración calificada.
  - #text(fill: ukj-blue)[*Mozambique*] @sorensen2020economic: se incluyó un modelo de gravedad como una forma de incorporar aspectos del lado de la demanda así como también modelos de pronósticos de exportaciones bilaterales.
  - #text(fill: ukj-blue)[*El Salvador*] @gomez2024complejidad: La identificación de actividades objetivo de diversificación se realizó mediante técnicas de Toma de Decisión Multiobjetivo, para posteriormente incluir criterios de viabilidad y atractivo. 
]


#slide[
  == Taller : Oportunidades Potenciales de Crecimiento. Atlas de Complejidad Económica.
    #figure(
      image("images/oportunidades_potenciales_crecimiento.png", width: 93%),
      caption : text(size: 10pt, font: "Lato")[Tomado del Atlas de Complejidad Económica. https://atlas.hks.harvard.edu/countries/188/growth-opportunities]
    ) 
]

#slide[
  == Taller : Oportunidades Potenciales de Crecimiento. Atlas de Complejidad Económica.

  - En el Atlas de Complejidad Económica se usan promedios ponderados de la Distancia, Complejidad y Ganancia de Oportunidad para identificar oportunidades de diversificación.
  - Definen tres estrategias de diversificación en los que se ponderan de forma distinta las tres medidas:
    - #text(fill: ukj-blue)[*Low-hanging Fruit*]:
      - Distancia : 60%
      - Complejidad : 15%
      - Ganancia de Oportunidad : 25
    - #text(fill: ukj-blue)[*Balanced Portfolio*]:
      - Distancia : 50%
      - Complejidad : 15%
      - Ganancia de Oportunidad : 35
    - #text(fill: ukj-blue)[*Long Jumps*]:
      - Distancia : 45%
      - Complejidad : 20%
      - Ganancia de Oportunidad : 35
]
#slide[
  #bibliography("references.bib",  style: "apa")
]



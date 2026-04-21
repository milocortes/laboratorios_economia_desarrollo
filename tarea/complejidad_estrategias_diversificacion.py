import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import polars as pl 
    import numpy as np
    import math
    import polars.selectors as cs
    import altair as alt
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Análisis de Complejidad para Zonas Metropolitanas de México

    Se proporcionan los datos de conteos de Unidades Económicas por rama de actividad del SCIAN y por Zona Metropolitana del Censo Económico de 2023 del INEGI.

    Los datos se encuentran en la ruta del repositorio `datos/pot_complexity_zm_2023.csv`. El esquema de los datos es el siguiente:
    * `zm` : Columna de Zona Metropolitana.
    * `rama_id` : Clave de la actividad a nivel de rama.
    * `industria` : Nombre de la clave de actividad.
    * `transable` : La columna toma valor igual a 1 si la actividad es transable.
    * `pot_total` : Población Ocupada Total.

    Con estos datos se solita realizar un análisis de complejidad para responder las siguientes preguntas:

    /// admonition | Preguntas a responder.

    * ¿Cuáles son las 10 Zonas Metropolitanas más Complejas?
    * ¿Cuáles son las 10 Industrias más Complejas?
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para responder a dichas preguntas, necesitas calcular los siguientes requerimientos:

    /// admonition | Secuencia de cálculos

    * Calcula RCA.
    * Calcula Matriz de Especialización Binaria $M$.
    * Calcula Matriz de Proximidad de las actividades industriales.
    * Calcula Diversidad y su respectiva matriz diagonal $D$.
    * Calcula Ubicuidad y su respectiva matriz diagonal $U$.
    * Calcula Densidad.
    * Calcula Distancia.
    * Calcula matrices de diversidad-ponderada $\tilde{M}$ para zonas metropolitanas e industrias.
    * Calcula los índices de Complejidad Económica (ICE) y Complejidad de las Industrias (ICI). Para esto, necesitas calcular lo siguiente:
        *  Calcular los eigenvectores y eigenvalores de las matrices $\tilde{M}$ de zonas metropolitanas e industrias.
        *  Ajusta el signo del ECI e ICI.
        *  Normaliza el ECI e ICI.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Oportunidades Potenciales de Crecimiento

    Definen tres estrategias de diversificación en los que se ponderan de forma distinta las tres medidas:

    * Low-hanging Fruit:
        * Densidad : 60%
        * Complejidad : 15%
        * Ganancia de Oportunidad : 25
    * Balanced Portfolio:
        * Densidad : 50%
        * Complejidad : 15%
        * Ganancia de Oportunidad : 35
    * Long Jumps:
        * Densidad : 45%
        * Complejidad : 20%
        * Ganancia de Oportunidad : 35

    Para cada portafolio, indica las 10 industrias que recomendarías promover a la Zona Metropolitana de tu elección.

    /// attention | Atención!

    * Calcula ganancia de oportunidad.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Opportunity Gain - Opportunity Outlook Gain (COG)

    - Podemos utilizar el opportunity value para calcular el beneficio potencial que obtendría un lugar si se especializa en una nueva actividad particular.
    - Se llama a este valor como la **ganancia de oportunidad (Opportunity Gain)** que un lugar $c$ obtendría de especializarse en la actividad $p$.
    - Se calcula como el cambio en el valor de oportunidad obtenido de especializarse en la actividad $p$.
    - La ganancia de oportunidad cuantifica la contribución de especializarse en una nueva actividad en términos de abrir las puertas a actividades cada vez más complejas.
    - Formalmente la calculamos como:

    \begin{equation}
    \text { opportunity gain }_c=\sum_{p^{\prime}} \frac{\phi_{p p^{\prime}}}{\sum_{p^{\prime \prime}} \phi_{p^{\prime \prime} p^{\prime}}}\left(1-M_{c p^{\prime}}\right) P C I_{p^{\prime}}
    \end{equation}

    >En la publicación **The atlas of economic complexity: Mapping paths to prosperity** se especifica la siguiente fórmula para el Opportunity Gain
    >
    \begin{equation}
    \text { opportunity gain }_c=\sum_{p^{\prime}} \frac{\phi_{p p^{\prime}}}{\sum_{p^{\prime \prime}} \phi_{p^{\prime \prime} p^{\prime}}}\left(1-M_{c p^{\prime}}\right) P C I_{p^{\prime}}-\left(1-d_{c p}\right) P C I_p
    \end{equation}

    > Aquí usaremos la especificación del glosario del portal del Atlas de Complejidad Económica ([liga](https://atlas.hks.harvard.edu/glossary))
    """)
    return


if __name__ == "__main__":
    app.run()

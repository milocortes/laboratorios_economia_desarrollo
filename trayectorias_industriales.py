import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Evolución de Trayectorias Industriales""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Relatedness
    - **Relatedness** mide la afinidad entre una ubicación y una actividad.
    - **Relatedness** se considera como un predictor de cambios en la especialización en la relación **ubicación-actividad** (Se espera que una buena medida de afinidad prediga cambios en los patrones de especialización).
    - La medida de **Relatedness** es construida usando **redes que conectan actividades similares**.
    - Formalmente, relatedness $\omega_{c,p}$ puede ser definido como un predictor de la matriz de especialización que satisface:

          $R_{c p}(t+\mathrm{d} t)=R_{c p}(t)+B \omega_{c p}(t)+\ldots$

    donde $B$ es un coeficiente positivo y significativo.

    - Hay muchas formas de medir el relatedness. Particularmente, se han hecho avances en lo que se conoce como **Relatedness Density**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Relatedness Density
    - **Relatedness Density** mira al número de actividades similares presentes en una ubicación.
    - Para calcular esta medida, primero definimos una **Proximidad**
    - Las medidas de proximidad conectan **parejas de actividades**, $\phi_{p p}$, o **parejas de ubicaciones**, $\phi_{cc}$.

    \begin{aligned}
      &\phi_{p p^{\prime}} \rightarrow \left\{\begin{array}{lll}
      \text{Product Space} \\
      \text{Industry Space} \\
      \text{Technology Space} \\
    \end{array}\right.\\
    \end{aligned}

    \begin{aligned}
      &\phi_{c c^{\prime}} \rightarrow \left\{\begin{array}{lll}
      \text{Country Space} \\
      \text{Producer Space} \\
      \end{array}\right.\\
    \end{aligned}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Relatedness Density

    - Hay múltiples formas de medir **Proximidad**. Algunas, como la **probabilidad condicional mínima**, miran a la colocalización o coaglomeración de actividades:

    \begin{equation}
    \phi_{p p^{\prime}}=\frac{\sum_c M_{c p} M_{c p^{\prime}}}{\max \left(M_p, M_{p,}\right)}
    \end{equation}

    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Relatedness Density
    - Con la medida de proximidad, podemos calcular **Relatedness Density** como la fracción de actividades relacionadas presentes en una ubicación

    \begin{equation}
    \omega_{c p}=\frac{\sum_{p\prime} M_{c p\prime} \phi_{p p^{\prime}}}{\sum_{p,} \phi_{p p^{\prime}}} 
    \end{equation}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## ¿La Densidad ayuda a predecir cambios en los patrones de especialización?

    Esperaríamos que en una regresión 

    \begin{equation}
    y_{l,a, t_1} = \beta_0 + \beta_1 \;  \omega_{l,a,t_0} + \beta_2 \; \text{RCA}_{l,a, t_0} + \delta_1 \;  \text{Lugar} + \delta_2 \; \text{Actividad} + \epsilon_{l,a, t_1} 
    \end{equation}

    el estimador $\beta_1$ resultara positivo y estadisticamente significativo. Los subíndices $l$ y $a$ corresponden al lugar y a la actividad, mientras que $t_0$ y $t_1$, donde $t_1 = t_0 + \Delta t$, corresponden a los años inicial y final del análisis (El $\Delta t$ suele considerarse de 5 a 10 años).

    La regresión controla por efectos fijos por Lugar y Actividad.

    Para este caso, la variable $y_{l,a,t_1}$ corresponderá a :

    - **Crecimiento del RCA** : variable continua igual a la inversa hiperbólica de la tasa de crecimiento del RCA entre 2015 y 2020.
    - **Aparición de industrias**: variable dicotómica que toma la etiqueta 1 si la industria tenía un RCA < 0.05 en 2015 y un RCA > 0.2 en 2020. En caso contrario, se asigna la etiqueta 0. La variable indica si la actividad se especializó en el periodo.
    - **Desaparición de industrias** : variable dicotómica que toma la etiqueta 1 si la industria tenía un RCA < 0.2 en 2015 y un RCA > 0.05 en 2020. En caso contrario, se asigna la etiqueta 0. La variable indica si la actividad perdió especialización en el periodo.
 

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


if __name__ == "__main__":
    app.run()

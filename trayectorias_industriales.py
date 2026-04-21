import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import polars as pl
    import numpy as np
    import pandas as pd
    return np, pd, pl


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

    - **Crecimiento del RCA** : variable continua igual a la tasa de crecimiento del RCA entre 2013 y 2023.
    - **Aparición de industrias**: variable dicotómica que toma la etiqueta 1 si la industria tenía un RCA < 1.0 en 2013 y un RCA >= 1.0 en 2023. En caso contrario, se asigna la etiqueta 0. La variable indica si la actividad se especializó en el periodo.
    - **Desaparición de industrias** : variable dicotómica que toma la etiqueta 1 si la industria tenía un RCA >= 1.0  en 2013 y un RCA < 1.0 en 2023. En caso contrario, se asigna la etiqueta 0. La variable indica si la actividad perdió especialización en el periodo.
    """
    )
    return


@app.cell
def _(pl):
    ### Cargamos datos de los Censos Económicos
    censos = pl.read_parquet("datos/mun_subs_03_23.parquet")

    ### Agregamos identificador de municipio
    censos = censos.with_columns(
        cve_geo_mun = pl.col("cve_ent").map_elements(lambda x : f"{x:02}") + pl.col("cve_mun").map_elements(lambda x : f"{x:03}"),
    )

    ### Eliminaremos algunos subsectores para utilizar posteriormente la Insumo Producto
    subsectores_elimina = [432, 433, 434, 435, 436, 437, 462, 463, 464, 465, 466, 467, 468, 469, 513, 516]

    censos = censos.filter(
        ~pl.col("subs_id").is_in(subsectores_elimina)
    )

    censos
    return (censos,)


@app.cell
def _(np, pd, pl):
    ### Funciones que calculan las medidas de complejidad
    def calcula_rca(
            datos : pl.DataFrame,
        activiy_col_name : str, 
        place_col_name : str,
        value_col_name : str,
        rca_umbral : float = 1.0, 
        ) -> pl.DataFrame:

        ## Calculamos RCA
        datos_rca = datos.with_columns(
        rca = (
            pl.col(value_col_name)/pl.col(value_col_name).sum().over(place_col_name)
        ) /
        (
            pl.col(value_col_name).sum().over(activiy_col_name)/pl.col(value_col_name).sum()
        )

        ).with_columns(
            pl.col(activiy_col_name).cast(pl.Int64)
        ).select(place_col_name, activiy_col_name, "rca")

        return datos_rca

    def calcula_densidad(
            datos : pl.DataFrame,
        activiy_col_name : str, 
        place_col_name : str,
        value_col_name : str,
        rca_umbral : float = 1.0, 
        proximity = None
        ) -> pl.DataFrame:

        ## Calculamos RCA
        datos_rca = calcula_rca(datos, activiy_col_name, place_col_name, value_col_name, rca_umbral)

        ## Calculamos matriz de especialización binaria M
        datos_rca_m = datos_rca.with_columns(
            M = pl.when(
                pl.col(activiy_col_name)>= rca_umbral   
            ).then(
                pl.lit(1)
            ).otherwise(
                pl.lit(0)
            )
        )

        M_df = datos_rca_m.pivot(activiy_col_name, 
                          index = place_col_name, 
                          values = "M"
                    ).fill_null(0).sort(place_col_name)

        ### Convertimos a un arreglo de numpy
        M = M_df.select(
            pl.exclude(place_col_name)
        ).to_numpy()

        ## Calculamos diversidad
        diversidad = M.sum(axis = 1)

        ## Calculamos ubicuidad
        ubicuidad = M.sum(axis = 0)

        ### Calculamos la proximidad
        if proximity is None:
            proximity = M.T @ M / ubicuidad[np.newaxis, :]  
            proximity = np.minimum(proximity, proximity.T)
            proximity = np.nan_to_num(proximity)

        ### Calculamos la densidad
        density = (np.dot(M,proximity)/np.sum(proximity, axis=1))
        density = np.nan_to_num(density)

        ### Convertimos el arreglo de numpy de la densidad a un dataframe
        actividades = [int(i) for i in M_df.columns[1:]]
        muni_claves = M_df.select(place_col_name).to_series().to_list()

        df_density = pl.from_pandas(
            pd.DataFrame(density
                     ,columns=actividades, 
                     index=muni_claves
                    ).reset_index().melt(
                        id_vars = "index"
                    ).rename(
                        columns={
                            "index" : place_col_name, 
                            "variable" : activiy_col_name, 
                            "value" : "density"
                        }
                    )
            )


        return df_density
    return calcula_densidad, calcula_rca


@app.cell
def _(calcula_densidad, calcula_rca, censos, pl):
    ### Calculamos la densidad de 2013 y los rca de 2013 y 2023
    activiy_col_name =  "subs_id"
    place_col_name = "cve_geo_mun"
    value_col_name = "Personal ocupado total"

    ### Censo 2023
    censo_2023 = censos.filter(
        pl.col("Año") == 2023
    )

    ### Censo 2013
    censo_2013 = censos.filter(
        pl.col("Año") == 2013
    )

    densidad_2013 = calcula_densidad(censo_2013, activiy_col_name, place_col_name, value_col_name)
    rca_2013 = calcula_rca(censo_2013, activiy_col_name, place_col_name, value_col_name).rename({"rca" : "rca_t0"})
    rca_2023 = calcula_rca(censo_2023, activiy_col_name, place_col_name, value_col_name).rename({"rca" : "rca_t1"})
    return (
        activiy_col_name,
        censo_2013,
        densidad_2013,
        place_col_name,
        rca_2013,
        rca_2023,
        value_col_name,
    )


@app.cell
def _(
    activiy_col_name,
    densidad_2013,
    np,
    pl,
    place_col_name,
    rca_2013,
    rca_2023,
):
    ## Reunimos los dataframes 
    df_regresiones = rca_2013.join(
        rca_2023, 
        on = [place_col_name, activiy_col_name]
    ).join(
        densidad_2013, 
        on = [place_col_name, activiy_col_name]
    )

    ## Creamos las columna de apariciones y desapariciones
    df_regresiones = df_regresiones.with_columns(
            ## Creamos variable de apariciones
            apariciones = pl.when(
                (pl.col("rca_t0") < 1.0) & (pl.col("rca_t1")>=1.0)
            ).then(
                pl.lit(1)
            ).otherwise(
                pl.lit(0)
            ), 
            ## Creamos variable de desapariciones
            desapariciones = pl.when(
                (pl.col("rca_t0") >= 1.0) & (pl.col("rca_t1")<1.0)
            ).then(
                pl.lit(1)
            ).otherwise(
                pl.lit(0)
            ), 
            ## Creamos variable de crecimiento del RCA (Log)
            growth_rca_log = np.log(pl.col("rca_t1")/pl.col("rca_t0")),
            ## Creamos variable de crecimiento del RCA (inversa hiperbólica de la tasa de crecimiento)
            growth_rca_arcsinh = np.arcsinh(pl.col("rca_t1")/pl.col("rca_t0")),

    )
    df_regresiones
    return (df_regresiones,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Usaremos el paquete [PyFixest](https://py-econometrics.github.io/pyfixest/quickstart.html) para estimar las regresiones.

    We can estimate a fixed effects regression via the feols() function. feols() has three arguments: a two-sided model formula, the data, and optionally, the type of inference.

    The first part of the formula contains the dependent variable and “regular” covariates, while the second part contains fixed effects.
    """
    )
    return


@app.cell
def _():
    import pyfixest as pf
    return (pf,)


@app.cell
def _(df_regresiones, pf):

    ### Regresión Growth RCA log - Con Efectos Fijos
    fit_rca_log = pf.feols(fml="growth_rca_log ~ rca_t0 + density | cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones)

    ### Regresión Growth RCA - Con Efectos Fijos
    fit_rca_arcsinh = pf.feols(fml="growth_rca_arcsinh ~ rca_t0 + density | cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones)

    ### Regresiones Apariciones - Sin Efectos Fijos
    fit_apariciones = pf.feglm(fml = "apariciones ~ density", data = df_regresiones, family = "logit", vcov="HC1")

    ### Regresiones Desapariciones - Sin Efectos Fijos
    fit_desapariciones = pf.feglm(fml = "desapariciones ~ rca_t0 + density", data = df_regresiones, family = "logit", vcov="HC1")
    return fit_apariciones, fit_desapariciones, fit_rca_arcsinh, fit_rca_log


@app.cell
def _(fit_apariciones, fit_desapariciones, fit_rca_arcsinh, fit_rca_log, pf):
    pf.etable([
        fit_rca_log, 
        fit_rca_arcsinh, 
        fit_apariciones, 
        fit_desapariciones
    ])
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Agreguemos variables explicativas adicionales 

    Para analizar la trayectoria de evolución industrial, a la forma funcional anterior agregamos como regresores las metricas de viabilidad:

    - **Relación Directa de Insumos (Input Presence)** : mide la presencia de actividades que producen insumos necesarios para las actividades.
    - **Relación Directa de Productos (Output Presence)** : mide la presencia de actividades que compran productos de las actividades.
    - **Similitud de industrias provedoras (Input Presence Similarity)** : mide la presencia de actividades que son similares respecto a la demanda de mismos insumos.
    - **Similitud de industrias compradoras (Output Presence Similarity)** : mide la presencia de actividades similares respecto a si le venden sus producción a las mismas industrias.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Relación Directa de Insumos

    La métrica expresa la presencia de actividades que producen insumos necesarios para las industrias. Es decir, trata de responder a la pregunta ¿están presentes las actividades que a las cuales las actividades les compran insumos?. Para la construcción de esta métrica se utilizó la [Matriz de Insumo Producto para México](https://www.inegi.org.mx/temas/mip/#informacion_general) de 2018 en precios constantes y la matriz de presencia-ausencia $M_{u,a}$.

    Para el cálculo de la metrica se utilizó la matriz de coeficientes técnicos , $A$, de la Matriz Insumo Producto. Siendo $Z$ la matriz de flujo entre sectores y $X$ es el vector de producto total, la matriz de coeficientes técnicos se calcularía como:

    \begin{equation}
    A= Z \cdot (X \cdot I)^{-1}
    \end{equation}

    Las entradas de la matriz $A$ definen los coeficientes técnicos como la proporción de insumo ofrecido por el sector $i$ y comprado por el sector $j$ con respecto al producto total del sector $j$, $a_{ij}= \dfrac{z_{ij}}{x_j}$.

    La presencia entre insumos utilizados por las actividades se calcularía como una medida de densidad donde la matriz de proximidad entre industrias, $\phi_{a,a'}$, se sustituye por la matriz de coeficientes técnicos:

    \begin{equation}
        \dfrac{ \sum_{a'}M_{ua'}A_{aa'}^{T} }{\sum_{a'} A^{T}_{aa'}}
    \end{equation}

    Dado que las columnas de la matriz de coeficientes técnicos representa la proporción de insumo ofrecido por el sector  $j$ y comprado por el sector $i$, transponemos la matriz para poder realizar el cálculo.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Relación Directa de Productos

    La métrica expresa la presencia de actividades que compran productos de las actividades. Es decir, trata de responder a la pregunta ¿están presentes las actividades que son clientes de los productos de las actividades? El cálculo es prácticamente el mismo que el de la medida de Relación Directa de Insumos. Sin embargo, dado que las entradas de la matriz de coeficientes técnicod corresponden a la proporción de insumo ofrecido por el sector $i$ y comprado por el sector $j$ con respecto al producto total del sector $j$, no es necesario transponer la matriz: 

    \begin{equation}
        \dfrac{ \sum_{a'}M_{ua'}A_{aa'} }{\sum_{a'} A_{aa'}}
    \end{equation}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Similitud de industrias provedoras

    La métrica expresa la presencia de actividades similares respecto a la demanda de mismos insumos. Es decir, trata de responder a la pregunta ¿están presentes industrias que demandan los mismos insumos? Para el cálculo de la medida se utilizó la matriz de coeficientes técnicos $A$ para realizar el cáculo *row wise correlation*, esto es, calcular la correlación para cada par de industrias para obtener una medida de similitud entre industrias de acuerdo a los insumos que utilizan.

    La presencia entre industrias que demandan insumos similares se calcularía como una medida de densidad donde la matriz de proximidad entre industrias, $\phi_{a,a'}$, se sustituye por la matriz de correlación entre pares de industrias de la matriz de coeficientes técnicos:

    \begin{equation}
        \dfrac{ \sum_{a'}M_{ua'}corr(A_{aa'}^T) }{\sum_{a'} corr(A_{aa'}^T)}
    \end{equation}

    Dado que las columnas de la matriz de coeficientes técnicos representa la proporción de insumo ofrecido por el sector  $j$ y comprado por el sector $i$, transponemos la matriz de coeficientes técnicos para calcular la correlación entre pares de industrias.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Similitud de industrias compradoras

    La métrica expresa la presencia de actividades similares respecto a si le venden sus producción a las mismas industrias. Es decir, trata de responder a la pregunta ¿están presentes industrias que tienen como clientes a las mismas activiades? Para el cálculo de la medida se utilizó la matriz de coeficientes técnicos $A$ para realizar el cáculo *column wise correlation*, esto es, calcular la correlación para cada par de industrias para obtener una medida de similitud entre industrias de acuerdo a las industrias que tienen como clientes.

    La presencia entre industrias que demandan insumos similares se calcularía como una medida de densidad donde la matriz de proximidad entre industrias, $\phi_{a,a'}$, se sustituye por la matriz de correlación entre pares de industrias de la matriz de coeficientes técnicos:

    \begin{equation}
        \dfrac{ \sum_{a'}M_{ua'}corr(A_{aa'}) }{\sum_{a'} corr(A_{aa'})}
    \end{equation}
    """
    )
    return


@app.cell
def _(pl):
    ### Cargamos la Matriz Insumo Producto y Eliminamos algunos sectores
    io = pl.read_csv("datos/io_2018_subsector.csv")
    io_subsectores_elimina = [111, 113, 511, 515, 814, 931]

    io = io.filter(
        (~pl.col("sector").is_in(io_subsectores_elimina)) & (~pl.col("variable").is_in(io_subsectores_elimina))
    )
    io
    return (io,)


@app.cell
def _(io, np):
    ## Obtengamos la matriz de flujo entre sectores o matriz de demanda interna
    Z = io.to_pandas().pivot(index = "sector", columns = "variable").to_numpy()

    # X es el vector de producto total
    X = Z.sum(axis =1) 

    ## Calculemos la matriz de coeficientes técnicos (matriz A)
    A = Z/X[:,None]

    #### Definimos una función para reescalar los valores mínimos y máximos de la matriz de correlación
    def reescala(valor):
        # scaled_fitness
        y = np.array([new_min, new_max])
        X = np.matrix([[min_val, 1],[max_val, 1]])

        try:
            a,b = np.ravel(X.I @ y)
        except:
            a,b = np.ravel(np.linalg.pinv(X) @ y)

        valor_reescalado = a*valor + b 

        return valor_reescalado

    reescala_vec = np.vectorize(reescala)

    ## Matriz de Similitud de industrias provedoras
    A_corr_insumos = np.corrcoef(A.T)

    max_val, min_val = np.max(A_corr_insumos), np.min(A_corr_insumos)
    new_max, new_min = 1.0, 0.0

    A_corr_insumos = reescala_vec(A_corr_insumos)

    ## Matriz de Similitud de industrias compradoras
    A_corr_clientes = np.corrcoef(A)

    max_val, min_val = np.max(A_corr_clientes), np.min(A_corr_clientes)

    A_corr_clientes = reescala_vec(A_corr_clientes)
    return A, A_corr_clientes, A_corr_insumos


@app.cell
def _(
    A,
    A_corr_clientes,
    A_corr_insumos,
    activiy_col_name,
    calcula_densidad,
    censo_2013,
    place_col_name,
    value_col_name,
):
    ### Calculamos medida de presencia de insumos
    presencia_insumos = calcula_densidad(censo_2013,
                                         activiy_col_name, 
                                         place_col_name, 
                                         value_col_name, 
                                         proximity = A.T).rename({"density" : "input_presente"})

    ### Calculamos medida de presencia de clientes
    presencia_clientes = calcula_densidad(censo_2013, 
                                          activiy_col_name, 
                                          place_col_name, 
                                          value_col_name, 
                                          proximity = A).rename({"density" : "output_presente"})

    ### Calculamos Input Presence Similarity
    # By default, numpy.corrcoef assumes rows are variables and columns are observations.
    # If your data has variables in columns and observations in rows,
    # you need to transpose the array or set rowvar=False.

    similaridad_insumos_presentes = calcula_densidad(censo_2013, 
                                                     activiy_col_name, 
                                                     place_col_name, 
                                                     value_col_name, 
                                                     proximity = A_corr_insumos).rename({"density" : "similaridad_input_presente"})

    ### Calculamos Output Presence Similarity
    similaridad_clientes_presentes = calcula_densidad(censo_2013, 
                                                      activiy_col_name, 
                                                      place_col_name, 
                                                      value_col_name, 
                                                      proximity = A_corr_clientes).rename({"density" : "similaridad_output_presente"})
    return (
        presencia_clientes,
        presencia_insumos,
        similaridad_clientes_presentes,
        similaridad_insumos_presentes,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Reunimos las variables estimadas""")
    return


@app.cell
def _(
    activiy_col_name,
    df_regresiones,
    place_col_name,
    presencia_clientes,
    presencia_insumos,
    similaridad_clientes_presentes,
    similaridad_insumos_presentes,
):
    df_regresiones_adicionales = df_regresiones.join(
        presencia_insumos, 
        on = [place_col_name, activiy_col_name]
    ).join(
        presencia_clientes, 
        on = [place_col_name, activiy_col_name]
    ).join(
        similaridad_insumos_presentes, 
        on = [place_col_name, activiy_col_name]
    ).join(
        similaridad_clientes_presentes, 
        on = [place_col_name, activiy_col_name]
    )
    return (df_regresiones_adicionales,)


@app.cell
def _(df_regresiones_adicionales, pf):
    ### Regresión Growth RCA log - Con Efectos Fijos
    fit_rca_log_adicionales = pf.feols(fml="growth_rca_log ~ rca_t0 + density + input_presente + output_presente| cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones_adicionales)

    ### Regresión Growth RCA - Con Efectos Fijos
    fit_rca_arcsinh_adicionales = pf.feols(fml="growth_rca_arcsinh ~ rca_t0 + density + input_presente + output_presente | cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones_adicionales)

    ### Regresiones Apariciones - Sin Efectos Fijos
    fit_apariciones_adicionales = pf.feglm(fml = "apariciones ~ density + input_presente + output_presente", data = df_regresiones_adicionales, family = "logit", vcov="HC1")

    ### Regresiones Desapariciones - Sin Efectos Fijos
    fit_desapariciones_adicionales = pf.feglm(fml = "desapariciones ~ rca_t0 + density + input_presente + output_presente", data = df_regresiones_adicionales, family = "logit", vcov="HC1")
    return (
        fit_apariciones_adicionales,
        fit_desapariciones_adicionales,
        fit_rca_arcsinh_adicionales,
    )


@app.cell
def _(df_regresiones_adicionales, pf):
    ### Regresión Growth RCA log - Con Efectos Fijos
    fit_rca_log_similares = pf.feols(fml="growth_rca_log ~ rca_t0 + density + similaridad_input_presente + similaridad_output_presente | cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones_adicionales)

    ### Regresión Growth RCA - Con Efectos Fijos
    fit_rca_arcsinh_similares = pf.feols(fml="growth_rca_arcsinh ~ rca_t0 + density + similaridad_input_presente + similaridad_output_presente | cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones_adicionales)

    ### Regresiones Apariciones - Sin Efectos Fijos
    fit_apariciones_similares = pf.feglm(fml = "apariciones ~ density + similaridad_input_presente + similaridad_output_presente", data = df_regresiones_adicionales, family = "logit", vcov="HC1")

    ### Regresiones Desapariciones - Sin Efectos Fijos
    fit_desapariciones_similares = pf.feglm(fml = "desapariciones ~ rca_t0 + density + similaridad_input_presente + similaridad_output_presente", data = df_regresiones_adicionales, family = "logit", vcov="HC1")
    return (
        fit_apariciones_similares,
        fit_desapariciones_similares,
        fit_rca_arcsinh_similares,
    )


@app.cell
def _(df_regresiones_adicionales, pf):
    ### Regresión Growth RCA log - Con Efectos Fijos
    fit_rca_log_completo = pf.feols(fml="growth_rca_log ~ rca_t0 + density + input_presente + output_presente + similaridad_input_presente + similaridad_output_presente | cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones_adicionales)

    ### Regresión Growth RCA - Con Efectos Fijos
    fit_rca_arcsinh_completo = pf.feols(fml="growth_rca_arcsinh ~ rca_t0 + density + input_presente + output_presente + similaridad_input_presente + similaridad_output_presente | cve_geo_mun + subs_id", vcov="HC1", data=df_regresiones_adicionales)

    ### Regresiones Apariciones - Sin Efectos Fijos
    fit_apariciones_completo = pf.feglm(fml = "apariciones ~ density + input_presente + output_presente + similaridad_input_presente + similaridad_output_presente", data = df_regresiones_adicionales, family = "logit", vcov="HC1")

    ### Regresiones Desapariciones - Sin Efectos Fijos
    fit_desapariciones_completo = pf.feglm(fml = "desapariciones ~ rca_t0 + density + input_presente + output_presente + similaridad_input_presente + similaridad_output_presente", data = df_regresiones_adicionales, family = "logit", vcov="HC1")
    return (
        fit_apariciones_completo,
        fit_desapariciones_completo,
        fit_rca_arcsinh_completo,
    )


@app.cell
def _(
    fit_apariciones,
    fit_apariciones_adicionales,
    fit_apariciones_completo,
    fit_apariciones_similares,
    fit_desapariciones,
    fit_desapariciones_adicionales,
    fit_desapariciones_completo,
    fit_desapariciones_similares,
    fit_rca_arcsinh,
    fit_rca_arcsinh_adicionales,
    fit_rca_arcsinh_completo,
    fit_rca_arcsinh_similares,
    pf,
):
    pf.etable([
        #fit_rca_log, 
        #fit_rca_log_adicionales, 
        #fit_rca_log_similares,
        fit_rca_arcsinh, 
        fit_rca_arcsinh_adicionales, 
        fit_rca_arcsinh_similares,
        fit_rca_arcsinh_completo,
        fit_apariciones, 
        fit_apariciones_adicionales, 
        fit_apariciones_similares,
        fit_apariciones_completo,
        fit_desapariciones,
        fit_desapariciones_adicionales, 
        fit_desapariciones_similares, 
        fit_desapariciones_completo
    ])
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

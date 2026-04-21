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
    import math
    import polars.selectors as cs
    import altair as alt
    return alt, cs, math, np, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Análisis de Complejidad para Zonas Metropolitanas de México

    Se proporcionan los datos de conteos de Unidades Económicas por rama de actividad del SCIAN y por Zona Metropolitana del Censo Económico de 2023 del INEGI.

    Los datos se encuentran en la ruta del repositorio `datos/complexity_zm_2023.csv`. El esquema de los datos es el siguiente:
    * `zm` : Columna de Zona Metropolitana.
    * `rama_id` : Clave de la actividad a nivel de rama.
    * `industria` : Nombre de la clave de actividad.
    * `transable` : La columna toma valor igual a 1 si la actividad es transable.
    * `ue` : Cantidad de Unidades Económicas.

    Con estos datos se solita realizar un análisis de complejidad para responder las siguientes preguntas:

    /// admonition | Preguntas a responder.

    * ¿Cuáles son las 10 Zonas Metropolitanas más Complejas?
    * ¿Cuáles son las 10 Industrias más Complejas?
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
    """
    )
    return


@app.cell
def _(pl):
    ## Cargamos datos
    datos = pl.read_csv("datos/complexity_zm_2023.csv")
    datos
    return (datos,)


@app.cell
def _(datos, pl):
    ## Calculamos RCA
    datos_rca = datos.with_columns(
        rca = (
            pl.col("ue")/pl.col("ue").sum().over("zm")
        ) /
        (
            pl.col("ue").sum().over("rama_id")/pl.col("ue").sum()
        )

    ).with_columns(
        pl.col("rama_id").cast(pl.Int64)
    )

    datos_rca
    return (datos_rca,)


@app.cell
def _(datos_rca, pl):
    ## Calculamos matriz de especialización binaria
    ## Umbral de RCA
    rca_umbral = 1.0

    datos_rca_m = datos_rca.with_columns(
        M = pl.when(
            pl.col("rca")>= rca_umbral   
        ).then(
            pl.lit(1)
        ).otherwise(
            pl.lit(0)
        )
    )
    datos_rca_m
    return (datos_rca_m,)


@app.cell
def _(datos_rca_m):
    ## Obtenemos la matriz M en formato dataframe
    M_df = datos_rca_m.pivot("rama_id", 
                      index = "zm", 
                      values = "M"
                ).fill_null(0).sort("zm")
    M_df
    return (M_df,)


@app.cell
def _(M_df, pl):
    ## Obtenemos la matriz M como arreglo de numpy
    M = M_df.select(
        pl.exclude("zm")
    ).to_numpy()

    M
    return (M,)


@app.cell
def _(M, np):
    ## Calculamos diversidad
    diversidad = M.sum(axis = 1)
    D = np.diag(diversidad)

    ## Calculamos ubicuidad
    ubicuidad = M.sum(axis = 0)
    U = np.diag(ubicuidad)
    return D, U, diversidad, ubicuidad


@app.cell
def _(M, np, ubicuidad):
    ## Calculamos matriz de Proximidad
    proximity = M.T @ M / ubicuidad[np.newaxis, :]  
    proximity = np.minimum(proximity, proximity.T)
    proximity = np.nan_to_num(proximity)
    proximity
    return (proximity,)


@app.cell
def _(M, np, proximity):
    ## Calculamos Densidad
    density = (np.dot(M,proximity)/np.sum(proximity, axis=1))
    density = np.nan_to_num(density)
    density
    return (density,)


@app.cell
def _(M, np, proximity):
    ## Calculamos Distancia
    distancia = (np.dot((1 - M),proximity)/np.sum(proximity, axis=1))
    distancia = np.nan_to_num(distancia)
    distancia
    return


@app.cell
def _(D, M, U, np):
    # Calculamos M tilde cc
    M_tilde_cc = np.linalg.pinv(D) @ M @ np.linalg.pinv(U) @ M.T
    M_tilde_cc 
    return (M_tilde_cc,)


@app.cell
def _(D, M, U, np):
    # Calculamos M tilde pp
    M_tilde_pp = np.linalg.pinv(U) @ M.T @ np.linalg.pinv(D) @ M
    M_tilde_pp 
    return (M_tilde_pp,)


@app.cell
def _(M_tilde_cc, np):
    ## Calculamos los eigenvectores y eigenvalores de la matriz M tilde cc
    eigenvalues_cc, eigenvectors_cc = np.linalg.eig(M_tilde_cc)

    ## Obtenemos el eigenvector asociado con el segundo eigenvalor más grande
    Kc = eigenvectors_cc[:, 1]

    Kc
    return (Kc,)


@app.cell
def _(M_tilde_pp, np):
    ## Calculamos los eigenvectores y eigenvalores de la matriz M tilde cc
    eigenvalues_pp, eigenvectors_pp = np.linalg.eig(M_tilde_pp)

    ## Obtenemos el eigenvector asociado con el segundo eigenvalor más grande
    Kp = eigenvectors_pp[:, 1].astype(float)

    Kp 
    return (Kp,)


@app.cell
def _(Kc, diversidad, math, np):
    ## Adjust sign of ECI and PCI so it makes sense, as per book
    corr_mat = np.corrcoef(diversidad, Kc)
    s1 = math.copysign(1.0, corr_mat[0,1])
    return (s1,)


@app.cell
def _(Kc, Kp, np, s1):
    ## Ajustamos y normalizamos ECI y PCI
    # La normalización usando usando la media y std ECI preserva
    # Que ---> ECI = (mean of PCI of products for which MCP=1)

    eci = s1*(Kc - np.mean(Kc))/np.std(Kc)
    pci = (Kp - np.mean(Kp))/np.std(Kp)
    return eci, pci


@app.cell
def _(M_df, datos, eci, pci, pl):
    ### Reunimos los datos calculados 
    df_eci = pl.DataFrame(
          {
            "zm" : M_df["zm"], 
            "eci" : eci, 
        }  
    )

    df_pci = pl.DataFrame(
          {
            "rama_id" : [int(i) for i in M_df.columns[1:]],
            "pci" : pci
        }  
    ).join(
        datos.select("rama_id", "industria").unique(), 
        on = "rama_id", 
        how = "inner"
    )
    return df_eci, df_pci


@app.cell
def _(df_eci):
    df_eci.sort(by="eci", descending=True)
    return


@app.cell
def _(df_pci):
    df_pci.sort(by="pci", descending=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
    """
    )
    return


@app.cell
def _(M, np, pci, proximity):
    ## Calculamos ganancia de oportunidad
    og = (proximity  @ ((proximity.sum(axis=1)**-1)[np.newaxis].T * (1 - M.T) * (pci[np.newaxis].T))).T
    og
    return (og,)


@app.cell
def _(M_df, cs, og, pl):
    ## Reunimos datos OG
    df_og = pl.DataFrame(og, schema = M_df.columns[1:])
    df_og = df_og.with_columns(
        zm = M_df["zm"]
    )
    df_og = df_og.unpivot(
                cs.numeric(),
                index = "zm"
            ).rename(
                {
                    "value" : "og", 
                    "variable" : "rama_id"
                }
        )
    df_og
    return (df_og,)


@app.cell
def _(M_df, cs, density, pl):
    ## Reunimos datos Distancia
    df_density = pl.DataFrame(density, schema = M_df.columns[1:])
    df_density = df_density.with_columns(
        zm = M_df["zm"]
    )
    df_density = df_density.unpivot(
                cs.numeric(),
                index = "zm"
            ).rename(
                {
                    "value" : "density", 
                    "variable" : "rama_id"
                }
        )
    df_density
    return (df_density,)


@app.cell
def _(datos_rca_m, df_density, df_og, df_pci, pl):
    ## Reunimos conjunto de datos 
    ### density y GO
    df_portafolios = df_density.join(
        df_og, 
        on = ["zm", "rama_id"]
    )

    ### Agregamos PCI
    df_portafolios = df_portafolios.join(
        df_pci.with_columns(pl.col("rama_id").cast(pl.String)), 
        on = "rama_id", 
        how = "left"
    )

    ### Agregamos especialización M
    df_portafolios = df_portafolios.join(
        datos_rca_m.select("zm", "rama_id", "M", "transable").with_columns(
            pl.col("rama_id").cast(pl.String)
        ),
        on = ["zm", "rama_id"]
    )

    ### Normalizamos density
    df_portafolios = df_portafolios.with_columns(
        density_norm = (pl.col("density") - pl.col("density").mean())/pl.col("density").std()
    )
    df_portafolios
    return (df_portafolios,)


@app.cell
def _(df_portafolios, np, pl):
    ## Calcula promedio ponderado de density, PCI y GO
    ### Define ponderadores
    product_selection_criteria = {
        "Low-hanging Fruit" : {"og" : 0.25, "pci" : 0.15, "density" : 0.60},
        "Balanced Portfolio" : {"og" : 0.35, "pci" : 0.15, "density" : 0.50},
        "Long Jumps" : {"og" : 0.35, "pci" : 0.20, "density" : 0.45},
    }

    ### Definimos portafolio
    portafolio = "Long Jumps"

    ### Creamos score como una media ponderada
    df_portafolios_score = df_portafolios.with_columns(
            df_portafolios.select(
                pl.struct("density_norm", "pci", "og").map_elements(
                    lambda s: np.average(
                        a = [s["density_norm"], s["pci"], s["og"]],
                        weights = [
                            product_selection_criteria[portafolio]["density"],
                            product_selection_criteria[portafolio]["pci"], 
                            product_selection_criteria[portafolio]["og"]
                        ]
                    ), 
                    return_dtype=pl.Float64
                ).alias("score")
            )
        )

    df_portafolios_score
    return (df_portafolios_score,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Para la Zona Metropolitana de Aguascalientes, ¿Cuales son la 10 industrias que no están especializadas con el Score más alto?""")
    return


@app.cell
def _(df_portafolios_score, pl):
    ### Define zm a analizar
    zm_nombre = "Zona metropolitana de Aguascalientes"
    #zm_nombre = "Metrópoli municipal de Acapulco"

    ### Nos quedamos con las industrias para las cuales no se encuentra especializada la región y ordenamos de acuerdo al score
    zm_industrias_portafolio = df_portafolios_score.filter(
        (pl.col("zm") == zm_nombre) &
        (pl.col("M") == 0) 
    )

    zm_industrias_portafolio = zm_industrias_portafolio.select(
        "zm", "rama_id", "industria", "score", "pci"
    ).sort("score", descending=True)

    zm_industrias_portafolio
    return (zm_industrias_portafolio,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Grafica relación del PCI con el Score calculado""")
    return


@app.cell
def _(alt, zm_industrias_portafolio):
    alt.Chart(zm_industrias_portafolio, title = "ICI vs Score").mark_circle(size=60).encode(
        x=alt.X('pci').title("ICI"),
        y=alt.Y('score').title("Score") ,
        tooltip=['industria', 'pci', 'score']
    ).interactive()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

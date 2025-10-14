import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Indentificación de Oportunidades de Diversificación""")
    return


@app.cell(hide_code=True)
def _():
    import polars as pl
    import pandas as pd
    import altair as alt
    import numpy as np
    return alt, np, pd, pl


@app.cell(hide_code=True)
def _(pl):
    ## Cargamos datos

    ### Growth Projections and Complexity Rankings (Rankings, HS92/HS12/SITC, 1962-2023)
    eci_rankings = pl.read_csv("datos/growth_proj_eci_rankings.csv")

    ### International Trade Data (HS92) (Unilateral Trade, HS92, 4 digit, 1995-2023)
    trade_data = pl.read_csv("datos/hs92_country_product_year_4_2023.csv")

    ### Classifications Data (Classifications, HS92, various years)
    hs92 = pl.read_csv("datos/product_hs92.csv", ignore_errors=True)
    return eci_rankings, hs92, trade_data


@app.cell(hide_code=True)
def _(hs92, pl, trade_data):
    ### Filtramos los productos que no están especializados (RCA < 1)
    trade_data_rca = trade_data.filter(
        pl.col("export_rca") < 1.0
    )

    ### Agregamos los nombres de los cluster a los que pertenece cada producto
    trade_data_rca = trade_data_rca.join(
        hs92.select("product_id", "product_name_short","product_parent_id"),
            left_on = "product_id",
            right_on = "product_id"
        ).rename(
            {
                "product_parent_id" : "product_id_2d", 
                "product_name_short" : "product_name"
            }
        ).join(
        hs92.select("product_id", "product_parent_id"),
            left_on = "product_id_2d",
            right_on = "product_id"
        ).rename(
            {
                "product_parent_id" : "product_id_1d"
            }
        ).join(
        hs92.select("product_id", "product_name_short"),
            left_on = "product_id_1d",
            right_on = "product_id"
        )     

    ### Normalizamos las variables de interes
    trade_data_rca = trade_data_rca.with_columns(
        distance_norm = (pl.col("distance") - pl.col("distance").mean())/pl.col("distance").std(),
        pci_norm = (pl.col("pci") - pl.col("pci").mean())/pl.col("pci").std(),
        cog_norm = (pl.col("cog") - pl.col("cog").mean())/pl.col("cog").std(),
        density = (1 - pl.col("distance"))
    )
    return (trade_data_rca,)


@app.cell(hide_code=True)
def _():
    ### Definimos diccionarios con los ponderadores de cada estrategia

    #### Product Selection Criteria
    product_selection_criteria = {
        "Low-hanging Fruit" : {"cog" : 0.25, "complexity" : 0.15, "distance" : 0.60},
        "Balanced Portfolio" : {"cog" : 0.35, "complexity" : 0.15, "distance" : 0.50},
        "Long Jumps" : {"cog" : 0.35, "complexity" : 0.20, "distance" : 0.45},
    }

    ### Complexity metrics
    complexity_metric = {
        "Complexity" : "pci",
        "Opportunity Gain" : "cog"
    }
    return complexity_metric, product_selection_criteria


@app.cell(hide_code=True)
def _(mo):
    ### Definimos Dropdowns

    #### Selection criteria dropdown
    drop_product_selection_criteria = mo.ui.dropdown(
        options=["Low-hanging Fruit", "Balanced Portfolio" , "Long Jumps"],
        value="Low-hanging Fruit",
        label="Choose Product Selection Criteria",
        searchable=True,
    )

    #### Complexity metric dropdown
    drop_complexity_metric =  mo.ui.dropdown(
        options=["Complexity", "Opportunity Gain"],
        value="Complexity",
        label="Choose Complexity Metric",
        searchable=True,
    )

    #### Country dropdown
    dropdown_country = mo.ui.dropdown(
        options=["BLZ", "MEX", "BRA", "GTM", "CRI"],
        value="BLZ",
        label="Choose Country",
        searchable=True,
    )
    return (
        drop_complexity_metric,
        drop_product_selection_criteria,
        dropdown_country,
    )


@app.cell(hide_code=True)
def _(
    drop_product_selection_criteria,
    dropdown_country,
    np,
    pl,
    product_selection_criteria,
    trade_data_rca,
):
    ## Filtra datos para el pais a analizar
    df_pais = trade_data_rca.filter(
        pl.col("country_iso3_code") == dropdown_country.value
    )

    ## Calcula promedio ponderado de Distancia, PCI y COG
    df_pais_plot = df_pais.with_columns(
            df_pais.select(
                pl.struct("density", "pci", "cog").map_elements(
                    lambda s: np.average(
                        a = [s["density"], s["pci"], s["cog"]],
                        weights = [
                            product_selection_criteria[drop_product_selection_criteria.value]["distance"],
                            product_selection_criteria[drop_product_selection_criteria.value]["complexity"], 
                            product_selection_criteria[drop_product_selection_criteria.value]["cog"]
                        ]
                    ), 
                    return_dtype=pl.Float32
                ).alias("score")
            )
        )


    return (df_pais_plot,)


@app.cell(hide_code=True)
def _(df_pais_plot, pl):
    ### Subset productos priorizados y no priorizados
    prioriza = df_pais_plot.sort(by="score", descending=True).select(pl.col("product_hs92_code").head(20)).to_series()

    #### Priorizados
    points_prioriza = df_pais_plot.filter(
                (pl.col("product_hs92_code").is_in(prioriza)) 
    )

    #### No Priorizados
    points_resto = df_pais_plot.filter(
                ~pl.col("product_hs92_code").is_in(prioriza)   
    )
    return points_prioriza, points_resto


@app.cell(hide_code=True)
def _(
    alt,
    complexity_metric,
    df_pais_plot,
    drop_complexity_metric,
    drop_product_selection_criteria,
    dropdown_country,
    eci_rankings,
    pd,
    pl,
    points_prioriza,
    points_resto,
    product_selection_criteria,
):
    # Create an Altair chart
    selection_weigths = ", ".join([f"{i} = {j}" for i,j in product_selection_criteria[drop_product_selection_criteria.value].items()])
    selection_weigths = "Weights : " + selection_weigths

    ### Priorized product plots
    relateness_plot_prioriza = alt.Chart(points_prioriza).mark_point().encode(
        alt.X('distance').scale(domain=(df_pais_plot["distance"].min(),df_pais_plot["distance"].max() + 0.005)), # Encoding along the x-axis
        alt.Y(complexity_metric[drop_complexity_metric.value]), # Encoding along the y-axis
        color='product_name_short', # Category encoding by color
        tooltip=['product_name', 'product_name_short', 'distance', complexity_metric[drop_complexity_metric.value]]
    ).properties(
        title = [f"Relatedness-complexity diagram - {dropdown_country.value} - Year : 2023", 
                 f"{drop_product_selection_criteria.value}", 
                selection_weigths],

    )

    ### Unpriorized product plots
    relateness_plot = alt.Chart(points_resto).mark_point(opacity=0.2).encode(
        alt.X('distance').scale(domain=(df_pais_plot["distance"].min(),df_pais_plot["distance"].max())), # Encoding along the x-axis
        alt.Y(complexity_metric[drop_complexity_metric.value]), # Encoding along the y-axis
        color='product_name_short', # Category encoding by color
        tooltip=['product_name', 'product_name_short', 'distance', complexity_metric[drop_complexity_metric.value]]
    )

    ### ECI horizontal line
    ECI_val_pais = eci_rankings.filter(
                        (pl.col("country_iso3_code") == dropdown_country.value) &
                        (pl.col("year") == 2023)
                    ).select("eci_hs92").to_series()

    line = alt.Chart(
        pd.DataFrame({'ECI': ECI_val_pais}
                    )).mark_rule().encode(y='ECI')

    return line, relateness_plot, relateness_plot_prioriza


@app.cell(hide_code=True)
def _(line, mo, relateness_plot, relateness_plot_prioriza):
    # Make it reactive ⚡
    relateness_plot_prioriza_mo = mo.ui.altair_chart(relateness_plot_prioriza)
    relateness_plot_mo = mo.ui.altair_chart(relateness_plot)
    line_mo = mo.ui.altair_chart(line)
    return line_mo, relateness_plot_mo, relateness_plot_prioriza_mo


@app.cell(hide_code=True)
def _(
    complexity_metric,
    drop_complexity_metric,
    drop_product_selection_criteria,
    dropdown_country,
    line_mo,
    mo,
    points_prioriza,
    relateness_plot_mo,
    relateness_plot_prioriza_mo,
):
    # In a new cell, display the chart and its data filtered by the selection

    if complexity_metric[drop_complexity_metric.value] == "pci":
        stack_plots = [
                    mo.hstack([dropdown_country]), 
                    drop_product_selection_criteria,drop_complexity_metric,
                    relateness_plot_prioriza_mo + relateness_plot_mo + line_mo,
                    points_prioriza
            ]
    else:
        stack_plots = [
                    mo.hstack([dropdown_country]), 
                    drop_product_selection_criteria,drop_complexity_metric,
                    relateness_plot_prioriza_mo + relateness_plot_mo,
                    points_prioriza
            ]

    mo.vstack(stack_plots)

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y
librerias de pandas para resolver las preguntas.
"""

from pandas import Series


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import pandas as pd

    df = pd.read_csv("./files/input/tbl1.tsv", sep="\t", index_col=False)

    resultado: list[str] = [i.capitalize() for i in sorted(df["c4"].unique())]

    return resultado


if __name__ == "__main__":
    print(pregunta_06())

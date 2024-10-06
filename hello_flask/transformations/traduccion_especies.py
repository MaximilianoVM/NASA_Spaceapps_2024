import pandas as pd

# Diccionario de traducción
traducciones = {
    'Oryza sativa': 'Arroz',
    'Zea mays': 'Maíz',
    'Triticum aestivum': 'Trigo',
    'Glycine max': 'Soya',
    'Solanum tuberosum': 'Papa'
}


# Función para aplicar la traducción
def traducir_especies(cultivo):
    for clave, valor in traducciones.items():
        if clave in cultivo:
            return valor
    return cultivo  # Si no encuentra coincidencia, devuelve el nombre original


def create_dataframe_trad(df: pd.DataFrame):
    # Aplicar la traducción a los valores del DataFrame
    df['Species_traducida'] = df['Species'].apply(traducir_especies)

    # Filtrar las filas donde 'Species_traducida' es diferente de 'Species' (es decir, fue traducido)
    df_traducido = df[df['Species'] != df['Species_traducida']]
    return df_traducido
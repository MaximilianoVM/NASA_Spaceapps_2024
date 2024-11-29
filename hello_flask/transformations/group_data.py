import pandas as pd

# Definir las funciones de agregación personalizadas
agg_funcs = {
    'Country': 'first',
    'Region': 'first',
    'Study_midyear': 'first',
    #'Site_name': 'first',
    'Species': lambda x: ', '.join(x.unique()),
    'Biome': 'first',
    'Leaf_habit': 'first',
    'Soil_drainage': 'first',
    'MAT': 'mean',
    'MAP': 'mean'
}

def group_data(df: pd.DataFrame):
    # Agrupar por 'Site_name' y 'Study_midyear' y aplicar las funciones de agregación
    grouped_df = df.drop(columns='Site_name')

    # Agrupar por 'Site_name' y 'Study_midyear' y aplicar las funciones de agregación
    grouped_df = grouped_df.groupby(['Region', 'Study_midyear']).agg(agg_funcs).reset_index(drop=True)

    return grouped_df
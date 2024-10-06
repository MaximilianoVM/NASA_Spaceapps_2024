import pandas as pd

PATH = '/home/max/workspace/NASA_Spaceapps_2024/data/DEF_SRDB_V5_1827_5-20241005_212220/srdb-data-V5.csv'
REL_PATH = 'hello_flask/data/DEF_SRDB_V5_1827_5-20241005_212220/srdb-data-V5.csv'

DATADIR_PATH = '/home/max/workspace/NASA_Spaceapps_2024/hello_flask/data'
DATADIR_REL_PATH = 'hello_flask/data/Processed'


to_keep = [
    'Entry_date', 
    'Quality_flag', 
    'Country', 
    'Region', 
    'Site_name', 
    'Site_ID', 
    'Study_midyear', 
    'Species', 
    'Biome', 
    'Ecosystem_type',
    'Leaf_habit', 
    'Soil_type', 
    'Soil_drainage', 
    'MAT', 
    'MAP', 
    'PET', 
    'Study_temp', 
    'Study_precip'
]

to_drop = [
    'Entry_date',
    'Quality_flag',
    'Ecosystem_type', 
    'Soil_type', 
    'PET', 
    'Study_temp', 
    'Study_precip', 
    'Site_ID'
]

# CONTIENE: 
# FILTRA COLUMNAS, DROPNA,  Study_midyear 1ra, SORT, EXPORTA
def create_dataframe_nasa():
    #df = pd.read_csv(RELATIVE_PATH, parse_dates=['Entry_date']).drop(columns=to_drop)
    #exporting the data
    #df.to_csv('clean_1_srdb-data-V5.csv', index=False)
    
    # Leer el archivo CSV y seleccionar solo las columnas especificadas                 # NA DROPPED
    df = pd.read_csv(REL_PATH, usecols=to_keep, parse_dates=['Entry_date']).drop(columns=to_drop).dropna()

    # Reorganizar las columnas para que 'Study_midyear' sea la primera
    columns = ['Study_midyear'] + [col for col in df.columns if col != 'Study_midyear']
    df = df[columns]

    # Ordenar el DataFrame por 'Study_midyear'
    df = df.sort_values(by='Study_midyear').reset_index(drop=True)
    
    # Exportar los datos
    df.to_csv(DATADIR_REL_PATH+'/Processed/1_prod_clean_srdb-data-V5.csv', index=False)
    
    return df
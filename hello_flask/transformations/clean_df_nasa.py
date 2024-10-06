import pandas as pd

PATH = '/home/max/workspace/NASA_Spaceapps_2024/data/DEF_SRDB_V5_1827_5-20241005_212220/srdb-data-V5.csv'
#RELATIVE_PATH = 'data/DEF_SRDB_V5_1827_5-20241005_212220/srdb-data-V5.csv'
RELATIVE_PATH = 'hello_flask/data/DEF_SRDB_V5_1827_5-20241005_212220/srdb-data-V5.csv'

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

def create_dataframe_nasa():
    df = pd.read_csv(RELATIVE_PATH, parse_dates=['Entry_date']).drop(columns=to_delete)
    #exporting the data
    df.to_csv('clean_1_srdb-data-V5.csv', index=False)
    
    return df
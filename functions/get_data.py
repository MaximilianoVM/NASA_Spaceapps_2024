import pandas as pd

PATH = '/home/max/workspace/NASA_Spaceapps_2024/data/DEF_SRDB_V5_1827_5-20241005_212220/srdb-data-V5.csv'
RELATIVE_PATH = 'data/DEF_SRDB_V5_1827_5-20241005_212220/srdb-data-V5.csv'

to_delete = ['Record_number', 
'Study_number', 
'Author',
'Contributor',
'Leaf_habit',
'Stage',
'Meas_method',
'Collar_height',
'Collar_depth',
'Chamber_area',
'Time_of_day',
'Partition_method'
]

df = pd.read_csv(PATH, parse_dates=['Entry_date']).drop(columns=to_delete)

#exporting the data
df.to_csv('clean_1_srdb-data-V5.csv', index=False)

# ============ GETS =================

def get_dataframe(): 
    return df

def get_countries_list():
    return df['Country'].unique()

def get_regions_by_country(country): # casi no hay regions (por lo menos en mexico)
    return df[ df['Country'] == country ]['Region'].unique()

def get_sites_by_region(region): # hay mas sites que country (por lo menos en mexico)
    return df[ df['Region'] == region ]['Site_name'].unique()

def get_sites_by_country(country):
    return df[ df['Country'] == country ]['Site_name'].unique()
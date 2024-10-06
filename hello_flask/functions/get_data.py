import pandas as pd
from transformations.clean_df_nasa import create_dataframe_nasa

df = create_dataframe_nasa()

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
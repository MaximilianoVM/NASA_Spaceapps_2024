#from transformations.group_data import group_data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#===================
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

#===================


def df_to_plot(df, country='USA', region='Massachusetts', site='hola'):
    # Filtrar el DataFrame por 'Country', 'Region' y 'Site_name'
    df_to_plot = df[
        (df['Country'] == country) & 
        (df['Region'] == region) #& 
        #(df['Site_name'] == site)
    ]
    
    # make Study_midyear begin at 0
    df_to_plot['Time_dummy'] = df_to_plot['Study_midyear'] - df_to_plot['Study_midyear'].min()
    
    #group
    df_to_plot = group_data(df_to_plot)
        
    return df_to_plot

df_dummy = pd.read_csv('hello_flask/data/Processed/to_plot_massachusetts.csv')

def make_plot(df_to_plot = df_dummy):
    
    fig, ax = plt.subplots()
    ax.plot('Time_dummy', 'MAP', data=df_dummy, color='0.75')
    ax = sns.regplot(x='Time_dummy', y='MAP', data=df_dummy, ci=None, scatter_kws=dict(color='0.25'))
    ax.set_title('MAP over time')

    return plt.show()


def plot_massachusettsTvM():
    fig, ax = plt.subplots()
    ax.plot('Time_dummy', 'MAT', data=df_dummy, color='0.75')
    ax = sns.regplot(x='Time_dummy', y='MAT', data=df_dummy, ci=None, scatter_kws=dict(color='0.25'))
    min_year = df_dummy['Study_midyear'].min()
    max_year = df_dummy['Study_midyear'].max()
    ax.set_title('temperature in degrees C over time from 1981.5 to 2011.5')
    return plt.show()

def plot_massachusettsTvT():
    fig, ax = plt.subplots()
    ax.plot('Time_dummy', 'MAP', data=df_dummy, color='0.75')
    ax = sns.regplot(x='Time_dummy', y='MAP', data=df_dummy, ci=None, scatter_kws=dict(color='0.25'))
    min_year = df_dummy['Study_midyear'].min()
    max_year = df_dummy['Study_midyear'].max()
    ax.set_title('precipitation in mm over time from 1981.5 to 2011.5')
    return plt.show()


plot_massachusettsTvM() # Temperature over time
plot_massachusettsTvT() # Precipitation over time
import re
from datetime import datetime

from flask import Flask, render_template, request

import pandas as pd
import numpy as np
import os 

import simplejson as json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import seaborn as sns

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from functions.get_data import *

app = Flask(__name__)

# Generate a scatter plot and returns the figure 
def get_plot(): 
    df = pd.read_csv('hello_flask/dummy_data/book_sales.csv', index_col="Date", parse_dates=['Date']).drop(columns='Paperback')

    df['Time'] = np.arange(len(df.index))

    # target = weight * time + bias

    # aqui construimos el grafico
    fig, ax = plt.subplots()
    ax.plot('Time', 'Hardcover', data=df, color='0.75')
    ax = sns.regplot(x='Time', y='Hardcover', data=df, ci=None, scatter_kws=dict(color='0.25'))
    ax.set_title('Time Plot of Hardcover Sales')

    # aqui desplegamos el grafico
    return plt

# Root URL 
@app.get('/dashboard') 
def single_converter(): 
    # Get the matplotlib plot  
    plot = get_plot() 

    # Save the figure in the static directory  
    plot.savefig(os.path.join('hello_flask','static', 'images', 'plot.png')) 

     # Close the figure to avoid overwriting 
    plot.close() 
    
    return render_template('dashboard.html', dashBoardActive = True, countries = get_countries_list()) 

# Create a JSON Encoder class
class json_serialize(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
    
# Root URL 
@app.route('/regions-by-country') 
def regions(): 
   return json.dumps({'result': get_regions_by_country(request.args.get('country'))}, cls=json_serialize)

# Root URL 
@app.route('/sites-by-region') 
def sites(): 
   return json.dumps({'result': get_sites_by_region(request.args.get('region'))}, cls=json_serialize)

# Root URL 
@app.route('/') 
@app.route('/home')
def home(): 
    return render_template('home.html', homeActive = True) 

@app.route('/models')
def models(): 
    return render_template('models.html', modelsActive = True) 

@app.route('/chat')
def chat(): 
    return render_template('chat.html', chatActive = True) 

@app.route('/sources')
def sources(): 
    return render_template('sources.html', sourcesActive = True) 
  
# Main Driver Function  
if __name__ == '__main__': 
    # Run the application on the local development server  
    app.run(debug=True) 
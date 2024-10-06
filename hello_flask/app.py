import re
from datetime import datetime

from flask import Flask, render_template

import pandas as pd
import numpy as np
import os 

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import seaborn as sns

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

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
    
    return render_template('dashboard.html', dashBoardActive = True) 

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
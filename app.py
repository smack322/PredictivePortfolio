import pandas as pd
import matplotlib.pyplot as plt
from flask import Response, send_file, Flask, render_template, send_from_directory, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
import requests

import os
app = Flask(__name__, static_folder='predictive-portfolio/build', static_url_path='/')

# Apply the proxy fix middleware to enable proxying
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route('/')

def index():
    return send_from_directory(app.static_folder, 'index.html')

def serve_file(path):
    return app.send_static_file(path)

@app.route('/api/apple')
def getAppleData():
    # Load data (replace 'your_data.csv' with your actual data file)
    appl_data = pd.read_csv('input_files/apple_data.csv')

    appl_data_json = appl_data.to_json(orient='records')
    
    # Basic analytics (customize as needed)
    # summary = appl_data.describe()
    
    # Basic plot (customize as needed)
    # plt.figure()
    # appl_data['your_column'].plot()
    # plt.savefig('static/plot.png')
    
    # Returning the summary as a string for demonstration (you might want to render it in an HTML template)
    return appl_data_json


@app.route('/api/microsoft')
def getMicrosoftData():
    # Load data (replace 'your_data.csv' with your actual data file)
    msft_data = pd.read_csv('input_files/microsoft_data.csv')
    
    msft_data_json = msft_data.to_json(orient='records')
    # Basic analytics (customize as needed)
    # summary = msft_data.describe()
    
    # Basic plot (customize as needed)
    # plt.figure()
    # msft_data['your_column'].plot()
    # plt.savefig('static/plot.png')
    
    # Returning the summary as a string for demonstration (you might want to render it in an HTML template)
    return msft_data_json

@app.route('/api/walmart')
def getWalmartData():
    # Load data (replace 'your_data.csv' with your actual data file)
    wlmt_data = pd.read_csv('input_files/microsoft_data.csv')
    
    wlmt_data_json = wlmt_data.to_json(orient='records')
    # Basic analytics (customize as needed)
    # summary = wlmt_data.describe()
    
    # # Basic plot (customize as needed)
    # plt.figure()
    # wlmt_data['your_column'].plot()
    # plt.savefig('static/plot.png')
    
    # Returning the summary as a string for demonstration (you might want to render it in an HTML template)
    return wlmt_data_json


if __name__ == '__main__':
    app.run(debug=False)

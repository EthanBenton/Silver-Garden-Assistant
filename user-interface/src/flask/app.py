from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ChooseYourPlant')
def ChooseYourPlant():
    # Add logic for the "Choose Your Plant" page
    return render_template('ChooseYourPlant.html')  # Create a new HTML template for this page

@app.route('/About')
def About():
    # Add logic for the "About" page
    return render_template('About.html')  # Create a new HTML template for this page

@app.route('/Home')
def Home():
    # Redirect to the "Index" page
    return redirect(url_for('index'))

@app.route('/graphs')
def graphs():
    # Add logic to generate and display your graphs
    return render_template('graphs.html')



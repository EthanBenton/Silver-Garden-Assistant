from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory

app = Flask(__name__, static_folder='src/flask/static')
app.secret_key = 'your_secret_key'  # Set a secret key for session encryption

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Solution statement and how PRIA works + MFCD
@app.route('/About')
def About():
    return render_template('About.html')

# Navigate back to homepage
@app.route('/Home')
def Home():
    return redirect(url_for('index'))

# Clickable box linking to the graphs
@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

# Settings page
@app.route('/settings')
def settings():
    return render_template('settings.html')

# User be able to add/remove plants
@app.route('/ChooseYourPlant', methods=['GET'])
def ChooseYourPlant():
    return send_from_directory('src/flask/static/js/react_app/ItemList', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)

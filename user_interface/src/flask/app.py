from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session encryption

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ChooseYourPlant', methods=['GET', 'POST'])
def ChooseYourPlant():
    if request.method == 'POST':
        plant = request.form.get('plants')
        if 'plants' not in session:
            session['plants'] = []  # Initialize an empty list if it doesn't exist
        if plant:
            session['plants'].append(plant)
    return render_template('ChooseYourPlant.html', plant_list=session.get('plants', []))

@app.route('/delete_plant/<int:index>')
def delete_plant(index):
    if 'plants' in session and 0 <= index < len(session['plants']):
        del session['plants'][index]
    return redirect(url_for('ChooseYourPlant'))

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Home')
def Home():
    return redirect(url_for('index'))

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')  # Assuming you have a settings.html file in your templates directory

if __name__ == "__main__":
    app.run(debug=True)
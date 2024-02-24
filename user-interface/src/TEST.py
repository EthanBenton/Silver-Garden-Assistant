from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ project_name }}</title>
        </head>
        <body>
            <h1>Welcome to {{ project_name }}</h1>
            <p>This is a simple Flask webpage.</p>
        </body>
        </html>
    """, project_name="PRIA")

if __name__ == "__main__":
    app.run(debug=True)
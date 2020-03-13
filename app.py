from flask import Flask, render_template, Response

app= Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

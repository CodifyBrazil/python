from flask import Flask, render_template

app = Flask("__main__")

@app.route('/')
def home():
    return render_template('home.html')


app.run(debug=True)
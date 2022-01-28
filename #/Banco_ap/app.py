from flask import Flask, render_template

app = Flask("__main__")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('Login.html')


app.run(debug=True)
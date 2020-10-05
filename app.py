from flask import Flask,render_template,url_for
import numpy as np
import pickle

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title='home',span='home')

@app.route('/python_project')
def python_project():
    return render_template("py_pro.html",title='Python Projects',span='python')

@app.route('/mini_project')
def mini_project():
    return render_template("mini_pro.html",title='Mini Project',span='home')

@app.route('/ml_project')
def ml_project():
    return render_template("ml_pro.html",title='ML Project',span='home')

@app.route('/deep_project')
def deep_project():
    return render_template("dl_pro.html",title='DL Project',span='home')

if __name__ == "__main__":
    app.run(debug=True)
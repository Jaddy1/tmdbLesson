from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    userData = dict(request.form)
    movieName = userData["movieName"]
    
    movie = model.movieSearch(movieName)
    
    # movieSearch = movieSearch["movieName"]
    return render_template("movieResult.html", movie = movie)
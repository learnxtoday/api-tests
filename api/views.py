from flask import Blueprint, jsonify, request
from . import db
from .models import Movie


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return """
        <pre>
        No UI. Run HTTP API calls only.
        1. http http://localhost:3000/movies
        2. http POST http://localhost:3000/add_movie
        </pre>
        """


@main.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])
    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201


@main.route('/movies')
def movies():

    movie_list = Movie.query.all()
    movies = []

    for movie in movie_list:
        movies.append({'title': movie.title, 'rating': movie.rating})

    return jsonify({'movies': movies})


@main.route('/delete/<movie_name>')
def delete(movie_name):
    if movie_name:
        exists = Movie.query.filter_by(title=movie_name).first()

    if exists:
        db.session.delete(exists)
        db.session.commit()

    result = 'Deleted {}'.format(exists.title)

    return result, 200

from flask import Blueprint, jsonify

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

    return 'Done', 201


@main.route('/movies')
def movies():

    movies = []

    return jsonify({'movies' : movies})


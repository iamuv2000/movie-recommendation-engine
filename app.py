#Module imports
from flask import Flask
from flask import render_template, jsonify, request
from movie_recommender import get_movie_recommendation
from flask_cors import CORS

# Creates a Flask application, named app
app = Flask(__name__)
cors = CORS(app)

# Route to get text summary
@app.route('/api/getRecommendations', methods=['POST'])
def api_all():
    movie_user_like = request.json['movie_user_like']
    no_of_movies = request.json['no_of_movies']
    print(movie_user_like)
    print(no_of_movies)
    movies = get_movie_recommendation(movie_user_like , no_of_movies)
    return jsonify(movies)


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
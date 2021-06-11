import sys
# print(sys.path)
# print()
sys.path.append("c:\\Users\\K Teja\\Documents\\3rd_year\\mini_project\\Flask_api\\youtube")
# print(sys.path)

from flask import Blueprint, jsonify, request
from extract import main_method
# print(can_you())
from . import db 
from .models import Movie


main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    # url=movie_data['url']
    link=movie_data['url']
    test=main_method(link)
    new_movie = Movie(url=movie_data['url'],video_title=test[2],percentage=test[0],thumbnail=test[3],description=test[1],channel_name=test[4])

    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201

@main.route('/movies')
def movies():
    movie_list = Movie.query.all()
    movies = []

    for movie in movie_list:
        movies.append({'url' : movie.url,'video_title':movie.video_title ,'percentage' : movie.percentage,'thumbnail':movie.thumbnail,'description':movie.description,'channel_name':movie.channel_name})

    return jsonify({'movies' : movies})
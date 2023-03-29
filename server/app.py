#!/usr/bin/env python3

# Standard library imports
import os
# Remote library imports
from flask import request, session, make_response, flash, redirect, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename


# Local imports
from config import app, db, api
from models import User, Song, CreatedSong, LikedSong

app.config['ALLOWED_EXTENSIONS'] = {'mp3'}
app.config['UPLOAD_FOLDER'] = 'static/'

# Views go here!
class Users(Resource):
    def get(self):
        user_dicts = [user.to_dict() for user in User.query.all()]

        return make_response(
            user_dicts,
            200
        )
    
class UserById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            return make_response({ 'error': 'User not found!' }, 404)
        
        return make_response(
            user.to_dict(),
            200
        )
    
class Songs(Resource):
    def get(self):
        song_dicts = [song.to_dict() for song in Song.query.all()]

        return make_response(
            song_dicts,
            200
        )
    
    def post(self):
        file = request.files['file']
        # extension = os.path.splitext(file.filename)[1]
        # import pdb; pdb.set_trace()
        print(file)
        new_song = Song(
            title=request.get_json()['title'],
            likes=0,
            genre=request.get_json()['genre'],
            # mp3=os.path.join(
            #     app.config['UPLOAD_FOLDER'],
            #     secure_filename(file.filename)
            # )
        )
        
        print(new_song)
        if file:
            # if extension not in app.config['ALLOWED_EXTENSIONS']:
            #     return 'File is not an mp3.'
            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'],
                secure_filename(file.filename)
            ))

        db.session.add(new_song)
        db.session.commit()

        return make_response(
            new_song.to_dict(),
            201
        )

    
class SongById(Resource):
    def get(self, id):
        song = Song.query.filter(Song.id == id).first()

        if not song:
            return make_response({ 'error': 'Song not found!' }, 404)
        
        return make_response(
            song.to_dict(),
            200
        )


class Signup(Resource):
    def post(self):
        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')

        user = User(
            username=username,
        )

        # the setter will encrypt this
        user.password_hash = password

        try:
            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            print(user.to_dict())

            return user.to_dict(), 201

        except IntegrityError:
            return {'error': '422 Unprocessable Entity'}, 422

class CheckSession(Resource):
    
    def get(self):

        if session.get('user_id'):

            user = User.query.filter(User.id == session['user_id']).first()

            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Login(Resource):
    
    def post(self):
        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')

        user = User.query.filter(User.username == username).first()

        if user:
            if user.authenticate(password):

                session['user_id'] = user.id
                return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Logout(Resource):
    
    def delete(self):
        
        if session.get('user_id'):
            
            session['user_id'] = None
            return {}, 204
        
        return {'error': '401 Unauthorized'}, 401
    

api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:id>')
api.add_resource(Songs, '/songs')
api.add_resource(SongById, '/songs/<int:id>')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

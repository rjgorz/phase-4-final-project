from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    created_songs = db.relationship('CreatedSong', backref='user')
    liked_songs = db.relationship('LikedSong', backref='user')

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    

    def __repr__(self):
        return f'<User {self.username}>'


class Song(db.Model, SerializerMixin):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String, nullable=False)
    mp3 = db.Column(db.String)

    created_songs = db.relationship('CreatedSong', backref='song')
    liked_songs = db.relationship('LikedSong', backref='song')

    def __repr__(self):
        return f'<Song {self.title}>'


class CreatedSong(db.Model, SerializerMixin):
    __tablename__ = 'created_songs'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'),nullable=False)

    def __repr__(self):
        return f'<Song {self.id}>'


class LikedSong(db.Model, SerializerMixin):
    __tablename__ = 'liked_songs'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'),nullable=False)

    def __repr__(self):
        return f'<Song {self.id}>'

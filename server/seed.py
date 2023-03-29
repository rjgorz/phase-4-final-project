#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
# from faker import Faker

# Local imports
from app import app
from models import db, Song

if __name__ == '__main__':
    # fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        test = Song(
            title="test",
            genre="test",
            likes=0,
            mp3='static/test.mp3'
        )

        db.session.add(test)
        db.session.commit()
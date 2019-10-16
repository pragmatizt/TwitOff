"""Entry point for our twitoff flask app"""

from .app import create_app
APP = create_app()

# remember - flask_sqlalchemy is what lets us add users from twitter onto our application

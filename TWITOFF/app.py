""" Main application for twitoff"""

# imports
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User
# from .models import DB, User

def create_app():
    """create and configures an instance of a flask app"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['ENV'] = config('ENV') # later should change to production
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False # this squelches the error messages
    ## 'sqlite:///db.sqlite3'
    # 'sqlite:///C://Users//evang//Desktop//TwitOff//TWITOFF//db.sqlite3'
    # 'sqlite:///C:\\Users\\evang\\Desktop\\TwitOff\\TWITOFF\\db.sqlite3'

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB Reset', users=[])
    return app

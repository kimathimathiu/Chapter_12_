import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE URL') or \
        'sqlite:///' + os.path.join(basedir, 'app db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER= os.environ.get('MAIL_SERVER')
    MAIL_PORT= int(os.environ.get('MAIL_PORT'))
    MAIL_USE_TLS= os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
    ADMIN= os.environ.get('ADMINS')
    POSTS_PER_PAGE= int(os.environ.get('POSTS_PER_PAGE'))
    
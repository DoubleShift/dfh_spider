import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(APP_ROOT, 'log.txt')

SECRET_KEY = 'dfh_spider_i73jdo9'

SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_ROOT, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(APP_ROOT, 'db_repository')



# custom object
ADDRESS_DSOURCE = 'http://46.101.30.187:5001/'

RESOURCE_ID = '100'

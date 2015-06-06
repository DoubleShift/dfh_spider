import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'dfh_spider_i73jdo9'

SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ROOT_PATH, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(ROOT_PATH, 'db_repository')


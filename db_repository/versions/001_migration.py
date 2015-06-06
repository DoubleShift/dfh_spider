from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
prices = Table('prices', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('pid', Integer),
    Column('price', Float),
    Column('date', Date),
)

products = Table('products', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('url', String(length=256)),
    Column('picture', String(length=256)),
    Column('stock', Integer),
    Column('date', Date),
    Column('score', String(length=8)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['prices'].create()
    post_meta.tables['products'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['prices'].drop()
    post_meta.tables['products'].drop()

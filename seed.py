"""Seed file to seed blogly_user_db"""

from models import User, db
from app import app

# create tables
db.drop_all()
db.create_all()

# if table is empty, empty it
User.query.delete()

# add pets
mikey = User(first_name='Michael', last_name="Aylmer", image_url='C70716D9-5180-4ADC-A5D0-9BA339D979CE_1_105_c.jpeg')


# add new object to session,
db.session.add(mikey)


# commit -otherwise, pointless
db.session.commit()

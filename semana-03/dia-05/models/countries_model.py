from db import db
from sqlalchemy import Column, Integer, String, Text

class CountriesModel(db.Model):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image = Column(Text)

    
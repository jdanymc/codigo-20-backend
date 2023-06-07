from db import db
from sqlalchemy import Column, Integer, String, Boolean

class JobsModel(db.Model):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    estado = Column(Boolean, default=True)
    salary = Column(String(50)) # $2000 - $3000
    type = Column(String(50))
    country_id = Column(Integer, db.ForeignKey('countries.id'))
    company_id = Column(Integer, db.ForeignKey('companies.id'))

    
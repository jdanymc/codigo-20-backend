from models.countries_model import CountriesModel
from db import db
from schemas.countries_schema import CountriesSchema

class CountriesController:
    def __init__(self):
        self.model = CountriesModel
        self.schema = CountriesSchema

    def getAll(self):
        try:
            records = self.model.query.all()
            data_schema = self.schema(many=True)
            return data_schema.dump(records),200
        except Exception as error:
            return {
                'message' : 'Error al crear el registro',
                'error' : str(error)
            },400
    def create(self, json):
        try:
            record = self.model(name=json['name'],image=json['image'])
            db.session.add(record)
            db.session.commit()

            return {
                'message' : 'Registro creado exitosamente'
            }, 201
            
        except Exception as error:
            return {
                'message' : 'Error al crear el registro',
                'error' : str(error)
            },400
        
   
        
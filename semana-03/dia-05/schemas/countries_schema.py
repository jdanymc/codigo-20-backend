from app import ma
from models.countries_model import CountriesModel

# class CountrysSchema(ma.Schema):
#     class Meta:
#         fields =('id', 'name', 'image')

class CountriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CountriesModel
from utils.db import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Product
class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product

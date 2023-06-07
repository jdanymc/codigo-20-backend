from flask import Blueprint, request
from controllers.countries_controller import CountriesController

countries_router = Blueprint('countries', __name__)
@countries_router.route('/countries', methods=['GET'])
def get_all_countries():
    controller = CountriesController()
    return controller.getAll()

@countries_router.route('/countries', methods=['POST'])
def create_countries():
    controller = CountriesController()
    return controller.create(request.get_json())

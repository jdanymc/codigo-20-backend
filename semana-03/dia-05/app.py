from flask import Flask
from db import db
from ma import ma
from flask_migrate import Migrate
#from flask_marshmallow import Marshmallow
#from models.users_model import UsersModel
#from models.companies_model import CompaniesModel
#from models.jobs_model import JobsModel

#from controllers.countries_controller import CountriesController

from routes.countries_router import countries_router
app = Flask(__name__)
migrate = Migrate(app, db)
#ma = Marshmallow(app)

app.app_context().push()
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456.a@localhost:3306/jobs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/jobs'

ma.init_app(app)
db.init_app(app)
#db.create_all()

@app.route('/')
def index():
    return 'Mi API de Flask funciona  '

app.register_blueprint(countries_router, url_prefix='/api-v1')
'''@app.route('/countries', methods=['GET','POST'])
def countries():
    controller = CountriesController()
    method = request.method
    if method == 'GET':
        return controller.getAll()
    else:
        return controller.create(request.get_json())    
'''
if(__name__ == '__main__'):
    app.run(debug=True)
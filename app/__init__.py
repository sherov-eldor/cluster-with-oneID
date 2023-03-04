from flask_sqlalchemy import SQLAlchemy
from flask_oneid import OneID
from flask import *


oneid = OneID()

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
oneid.init_app(app)


with app.app_context():
    # db.drop_all()
    db.create_all()

from app import route


with app.test_request_context():
    oneid.Set_Callback(url_for('get_params'))


# app = Flask(__name__)
# app.config.from_pyfile('config.py')
# db = SQLAlchemy(app)

# from app import route

# with app.app_context():
#     # db.drop_all()
#     db.create_all()




# from flask_oneid import OneID
# from flask import *
# def create_app():
#     oneid = OneID()
#     app = Flask(__name__)
#     app.config.from_pyfile('config.py')
#     oneid.init_app(app)
    
#     @app.route("/", methods=['GET'])
#     def index():
#         return "Hello World"
#     @app.route("/params", methods=['GET'])
#     def params():
#         data = oneid.Params_To_Dict(request.args)
#         return jsonify(data)
    
#     with app.test_request_context():
#         oneid.Set_Callback(url_for('params'))
#     return app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)


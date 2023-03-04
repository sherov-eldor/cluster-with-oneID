from flask.views import MethodView
from flask import current_app
class OneIDAPI(MethodView):

    def get(self):
        
        pass


app.add_url_rule('/users/', view_func=OneIDAPI.as_view('users'))
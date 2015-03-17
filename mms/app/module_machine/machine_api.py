from flask import Blueprint,url_for,redirect,session
from app import app
from flask.views import View, MethodView
import json 


machine_api= Blueprint('machine_api', __name__)

class test(MethodView):
    def get(self):
        return (json.dumps({"msg":"hello world this is from get request"}))

    def post(self):
        return json.dumps({"msg":"hello world this is from post request"})

machine_api.add_url_rule('/test', view_func=test.as_view('test'), methods=['GET', 'POST']) 

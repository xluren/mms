from flask import Flask
from flask.ext.sqlalchemy  import SQLAlchemy
from flask import request
import json

app = Flask(__name__)

app.config.from_object("config.Config")
db=SQLAlchemy(app)

from app.common.db_model.models import *

@app.route("/")
def main():

    method=json.loads(request.data)["method"]
    params=json.loads(request.data)["params"]


    class_name=method.split('.')[0]
    table_name=class_name
    func_name=method.split('.')[1]

    obj=__import__("app.module_%s.%s" % (class_name,class_name),fromlist=["app.module_%s.%s" %(class_name,class_name)])

    cls=getattr(obj,class_name)
    obj=cls(table_name,params)

    method=getattr(obj,func_name)
    result=method()

    return result

db.create_all()
print app.url_map


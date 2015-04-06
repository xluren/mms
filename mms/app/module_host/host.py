from flask import request
from app import app,db
from app.common.db_model.models import host
from app.module_origine.origine import origine
import json 

class host(origine):
    pass

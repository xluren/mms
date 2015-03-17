from flask import Flask

app = Flask(__name__)

app.config.from_object("config")

from app.module_machine.machine_api import machine_api 

app.register_blueprint(machine_api,url_prefix='/machine_api')

print app.url_map


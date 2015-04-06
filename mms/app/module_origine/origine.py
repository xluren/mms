from flask import request
from app import db
from app.common.db_model.models import host
import json 

class origine(object):
    
    def select(self,table_name,params):
        output_keys         = params["output"]
        filter_condition    = params["filter"]

        sql=",".join(output_keys)
        where=""

        for key,value in  filter_condition.items():
            where+='%s in ( "' % key +'","'.join(value)+'") and '

        return "select %s from host where %s" %(sql,where[0:-4])

    def delete(self,table_name,params):
        where=""

        for key,value in  params.items():
            where+='%s in ( "' % key +'","'.join(value)+'") and '

        return "delete from host where %s" %(where[0:-4])

    def update(self,table_name,params):
        hostid  = params["hostid"]
        del params["hostid"]
        print json.dumps(params,indent=2)
        print type(params).__name__
        return "update host"

    def insert(self,table_name,params):
        from app.common.db_model.models import host
        obj=__import__("app.common.db_model.models" ,fromlist=["app.common.db_model.models"])
        cls=getattr(obj,table_name)
        print "#"
        print cls.__mapper__.columns.keys()
        print "#"
        print dir(cls)
        instance=cls(params)
        db.session.add(instance)
        db.session.commit()
        print db.session.query(cls).filter().all()
        print json.dumps(params,indent=2)
        return "this is host insert"

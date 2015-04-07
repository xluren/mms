from flask import request
from app import db
from app.common.db_model.models import host
import json 

class origine(object):
    
    def select(self,table_name,params):
        output_keys         = params["output"]
        filter_condition    = params["filter"]

        select_item=",".join(output_keys)
        where_condition=""

        for key,value in  filter_condition.items():
            where_condition+='%s in ( "' % key +'","'.join(value)+'") and '


        obj=__import__("app.common.db_model.models" ,fromlist=["app.common.db_model.models"])
        cls=getattr(obj,table_name)
        result=db.session.execute("select %s from %s where %s " %(select_item,table_name,where_condition[0:-4]))

        result_list=[]

        for item in result:
            result_list.append(dict(zip(output_keys,item)))
        
        return json.dumps({"result":result_list},indent=2)


    def delete(self,table_name,params):

        filter_condition=params["filter"]
        where_condition=""

        for key,value in  filter_condition.items():
            where_condition+='%s in ( "' % key +'","'.join(value)+'") and '

        obj=__import__("app.common.db_model.models" ,fromlist=["app.common.db_model.models"])
        cls=getattr(obj,table_name)

        for item in db.session.query(cls).filter(where_condition[0:-4]).all():
            db.session.delete(item)
        db.session.commit()
        return "delete from host where %s" %(where_condition[0:-4])

    def update(self,table_name,params):
        filter_condition    = params["filter"]
        update_dict         = params["update_dict"]
        where_condition     = ""


        for key,value in  filter_condition.items():
            where_condition+='%s in ( "' % key +'","'.join(value)+'") and '

        obj=__import__("app.common.db_model.models" ,fromlist=["app.common.db_model.models"])
        cls=getattr(obj,table_name)

        print where_condition[0:-4]
        print update_dict
        print db.session.query(cls).filter(where_condition[0:-4]).all() 
        print "#################"
        print db.session.query(cls).filter(where_condition[0:-4]).update(update_dict,synchronize_session=False)
        db.session.commit()
        print "#################"
        print db.session.query(cls).filter().all()
        print json.dumps(params,indent=2)
        print type(params).__name__
        return "update host"

    def insert(self,table_name,params):
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

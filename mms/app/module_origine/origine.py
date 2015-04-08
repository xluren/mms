from flask import request
from app import db
import json 

class origine(object):
    
    def __init__(self,table_name,params):

        obj=__import__("app.common.db_model.models" ,fromlist=["app.common.db_model.models"])

        self.cls=getattr(obj,table_name)
        self.params=params
        self.table_name=table_name

        if params.has_key("filter"):
            filter_condition    = self.params["filter"]
            condition=""
            for key,value in  filter_condition.items():
                condition+='%s in ( "' % key +'","'.join(value)+'") and '
            self.where_condition=condition[0:-4] 

    def select(self):

        print self.params
        output_keys = self.params["output"]

        select_item=",".join(output_keys)

        result=db.session.execute("select %s from %s where %s " %(select_item,self.table_name,self.where_condition))
        result_list=[]
        
        for item in result:
            result_list.append(dict(zip(output_keys,item)))
        return json.dumps({"result":result_list},indent=2)


    def delete(self):

        for item in db.session.query(self.cls).filter(self.where_condition).all():
            db.session.delete(item)
        db.session.commit()
        return "delete from host where %s" %(self.where_condition)

    def update(self):

        update_dict  = params["update_dict"]

        db.session.query(self.cls).filter(self.where_condition).update(update_dict,synchronize_session=False)
        db.session.commit()
        return "update host"

    def insert(self):

        instance=self.cls(self.params)
        db.session.add(instance)
        db.session.commit()
        return "this is host insert"

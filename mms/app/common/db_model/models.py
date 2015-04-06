from app import db

from passlib.apps import custom_app_context as password_context

class user(db.Model):

    __tablename__ = 'user'

    useid       = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(32))
    password    = db.Column(db.String(64))

    def __init__(self, init_dict):
        self.name       = init_dict["name"]
        self.password   = self.hash_password(init_dict["password"])

    def hash_password(self, password):
        return password_context.encrypt(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password)

    def set_password(self, password):
        self.password=self.hash_password(password)

class service(db.Model):

    __tablename__   = "service"

    serviceid   = db.Column(db.Integer,primary_key=True,index=True)
    name        = db.Column(db.String(20))
    servicefid  = db.Column(db.Integer)

    def __init__(self,init_dict):
        self.name       = init_dict["name"]
        self.servicefid = init_dict["servicefid"]

    def __repr__(self):
        return "<service info %r,%r,%r>" % (self.serviceid,self.name,self.servicefid)


class permission(db.Model):

    __tablename__ = 'permission'

    id          = db.Column(db.Integer, primary_key=True)
    userid      = db.Column(db.Integer)
    serviceid   = db.Column(db.Integer)
    permission  = db.Column(db.String(5))

    def __init__(self, init_dict):
        self.userid     = init_dict["userid"]
        self.serviceid  = init_dict["serviceid"]
        self.permission = init_dict["permission"]

class host(db.Model):

    __tablename__="host"

    hostid      =   db.Column(db.Integer,primary_key=True)
    hostname    =   db.Column(db.String(64))
    hostip      =   db.Column(db.String(25))
    '''
    kernal      =   db.Column(db.String(28))

    description =   db.Column(db.String(28))
    carrier     =   db.Column(db.String(15))
    
    cpus        =   db.Column(db.Integer)
    rams        =   db.Column(db.Integer)
    disk        =   db.Column(db.Integer)

    city        =   db.Column(db.String(28))
    idc         =   db.Column(db.String(28))
    '''
    serviceids  =   db.Column(db.String(28))

    def __init__(self,init_dict):
        for attr in self.__mapper__.columns.keys():
            if attr!='hostid':
                setattr(self,attr,init_dict[attr])


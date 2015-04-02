from app import db
from passlib.apps import custom_app_context as password_context

class Service(db.Model):

    __tablename__   = "service"

    id      = db.Column(db.Integer,primary_key=True,index=True)
    name    = db.Column(db.String(20))
    fid     = db.Column(db.Integer)

    def __init__(self,name,fid):
        self.name   = name
        self.fid    = fid
    def __repr__(self):
        return "<service info %r,%r,%r>" % (self.id,self.name,self.fid)

class User(db.Model):

    __tablename__ = 'user'

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(32))
    password   = db.Column(db.String(64))
    serviceid  = db.Column(db.Integer)
    permission = db.Column(db.String(5))

    def __init__(self, name, password,serviceid,permission):
        self.name       = name
        self.password   = self.hash_password(password)
        self.serviceid  = serviceid
        self.permission = permission

    def hash_password(self, password):
        return password_context.encrypt(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password)

    def set_password(self, password):
        self.password=self.hash_password(password)

class Host(db.Model):

    __tablename__="host"

    id          =   db.Column(db.Integer,primary_key=True)
    hostname    =   db.Column(db.String(64))
    hostip      =   db.Column(db.String(25))
    kernal      =   db.Column(db.String(28))
    description =   db.Column(db.String(28))
    carrier     =   db.Column(db.String(15))
    
    cpus        =   db.Column(db.Integer)
    rams        =   db.Column(db.Integer)
    disk        =   db.Column(db.Integer)
    
    serviceids  =   db.Column(db.String(28))

    def __init__(self,hostname,hostip,kernal,
                    description,carrier,
                    cpus,rams,disk,serviceids):
        self.hostname       = hostname
        self.hostip         = hostip 
        self.kernal         = kernal 
        self.description    = description
        self.carrier        = carrier 
        self.cpus           = cpus 
        self.rams           = rams 
        self.disk           = disk 
        self.serviceids     = serviceids 

from app import db
from passlib.apps import custom_app_context as password_context

class Service(db.Model):
    __tablename__   = "service_table"

    service_id      = db.Column(db.Integer,primary_key=True,index=True)
    service_name    = db.Column(db.String(20))
    service_fid     = db.Column(db.Integer)
    group_id        = db.Column(db.Integer)
    owner_ids       = db.Column(db.String(28))

    def __init__(self,service_name,service_fid,group_id,owner_ids):
        self.service_name   = service_name
        self.service_fid    = service_fid
        self.group_id       = group_id
        self.owner_ids      = owner_ids
    def __repr__(self):
        return "<service info %r,%r,%r>" % (self.service_id,self.service_name,self.servic_fid)

class User(db.Model):
    __tablename__ = 'user_table'
    user_id         = db.Column(db.Integer, primary_key=True)
    user_name       = db.Column(db.String(32), index=True,unique=True)
    user_password   = db.Column(db.String(64))
    user_groupid    = db.Column(db.Integer)

    def __init__(self, name, password,groupid):
        self.user_name      = username
        self.user_groupid   = service_id
        self.user_password  = self.hash_password(password)

    def hash_password(self, password):
        return password_context.encrypt(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password)

    def set_password(self, password):
        self.password=self.hash_password(password)

    def set_user_name(self, user_name):
        self.username=username

    def set_service_id(self,service_id):
        self.service_id=service_id


class Config(object):
	DEBUG=False
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/sql_test.db'
	CSRF_ENABLED=True
	CSRF_SESSION_KEY="secret"
	SECRER_KEY="hello secret key"
class MysqlConfig(Config):
	SQLALCHEMY_DATABASE_URI='mysql://hello:hello@10.210.71.145:3306/sqlalchemy'
	DEBUG=True
class TestConfig(Config):
	DEBUG=True

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = "liu_qa"
USERNAME = 'root'
PASSWORD = 'root'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "root"


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG : True
MAIL_USERNAME = "hl15050556678@qq.com"

"""
MAIL_PASSWORD : default None
"""

MAIL_DEFAULT_SENDER = "hl15050556678@qq.com"


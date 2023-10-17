from random import sample


SECRET_KEY = '123456'

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@10.254.12.55:3306/zyb_app_test'


# email
MAIL_CODE = ''.join(sample('123456789', 6))
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'm13241276769@163.com'
MAIL_PASSWORD = 'WACWGXMSAENFLFZS'
MAIL_CONTENT = '你的验证码为: %s,请注意查收'
MAIL_TITLE = '注册信息'

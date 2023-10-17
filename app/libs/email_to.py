from flask_mail import Mail, Message


mail = Mail()


class email:
    def __init__(self):
        self.message = ''
        self.code = ''

    def send_email(self, acceptor):
        from app.manage import app
        self.code = app.config['MAIL_CODE']
        self.message = app.config['MAIL_CONTENT'] % self.code
        msg = Message(app.config['MAIL_TITLE'], sender='m13241276769@163.com', body=self.message,
                      recipients=[acceptor])
        try:
            mail.send(msg)
            return True
        except Exception as e:
            raise False

    @staticmethod
    def into_code(data):
        from app.manage import app
        app.config['ROCK_CODE'] = data

    @staticmethod
    def code_compare(code, rcode):
        if code == str(rcode):
            return True
        else:
            return False
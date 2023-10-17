# handle upload
import os

from werkzeug.utils import secure_filename

from app.manage import app
from app.view_model.device.device import DeviceMessage

message = DeviceMessage()

class upload:
    # def __init__(self):
    #     self.
    @staticmethod
    def upload(file):
        filename = secure_filename(file.filename)
        if filename.endswith('apk'):
            apk = app.config['APK_UPLOAD_PATH'] + filename
            app.config['REMOTE_ADDR'] = apk
            try:
                file.save(apk)
                message.success()
            except Exception as e:
                message.fail(e)
        elif filename.endswith('xlsx'):
            xlsx = app.config['XLSX_UPLOAD_PATH'] + filename
            try:
                cmd = 'find %s -type f -delete' % app.config['XLSX_UPLOAD_PATH']
                os.system(cmd)
                try:
                    file.save(xlsx)
                    message.success()
                except Exception as e:
                    message.fail(e)
            except Exception as e:
                message.fail(e)
        elif filename.endswith('txt'):
            txt = app.config['TXT_UPLOAD_PATH'] + filename
            try:
                cmd = 'find %s -type f -delete' % app.config['TXT_UPLOAD_PATH']
                os.system(cmd)
                try:
                    file.save(txt)
                    message.success()
                except Exception as e:
                    message.fail(e)
            except Exception as e:
                message.fail(e)
        return message.message


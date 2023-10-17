from flask import request
from flask_login import login_required
from werkzeug.utils import secure_filename

from . import general


@general.route('/upload', methods=['GET', 'POST'])
# @login_required
def uploads():
    from app.libs.up import upload
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        s = upload()
        return s.upload(f)







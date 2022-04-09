import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/UplodedFiles'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for file in request.files.getlist('file_name'):
        # check if the post request has the file part
            #f=request.files['file_name']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return render_template('home.html',msg="file has been uploaded successfuly")
    return render_template('home.html',msg="Please Choose a file")


if __name__=='__main__':
    app.run(debug=True)
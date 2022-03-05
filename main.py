import requests
from flask import Flask, render_template, request, url_for, flash, redirect
import settings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'  # à renseigner


@app.route('/')
def index():
    return render_template('index.html')


def post_rds(classes, teacherName, hoursNumber, description):
    data = {'classes': classes, 'teacherName': teacherName, 'hoursNumber': hoursNumber, 'description': description}
    r = requests.post(
        url=settings.url,
        json=data
    )


def post_s3(document):
    data = {'document': document}
    r = requests.post(
        url=settings.url,
        json=data
    )


@app.route('/index', methods='POST')
def index():
    if request.method == 'POST':
        classes = request.form['classes']
        teacherName = request.form['teacherName']
        hoursNumber = request.form['hoursNumber']
        description = request.form['description']
        document = request.form['document']

        if document:
            post_s3(document)
            return redirect(url_for('index'))
        else:
            post_rds(classes, teacherName, hoursNumber, description)
            return redirect(url_for('index'))

    return render_template('index.html')

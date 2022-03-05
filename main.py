import requests
from flask import Flask, render_template, request, url_for, flash, redirect
import settings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'  # à renseigner


@app.route('/')
def index():
    return render_template('index.html')


def post_rds(classes, teacherName, hoursNumber, description, document, storages):
    data = {'class': classes, 'teacherName': teacherName, 'hoursNumber': hoursNumber, 'description': description,
            'document': document, 'storages': storages}
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
        storages = request.form['storages']

        if not classes or storages:
            flash('Un nom de cours et un type de stockage est requis est requis')
        else:
            post_rds(classes, teacherName, hoursNumber, description, document, storages)
            return redirect(url_for('index'))

    return render_template('index.html')

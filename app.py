import requests
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'  # à renseigner

url_rds = "http://127.0.0.1:8000/rds"
url_s3 = "http://127.0.0.1:8000/s3"


def post_rds(subject: str, teacher_name: str, hours_numbers: str, description: str):
    data = {'subject': subject,
            'teacher_name': teacher_name,
            'hours_numbers': hours_numbers,
            'description': description}
    print("Posting to RDS")
    res = requests.post(
        url=url_rds,
        json=data
    )

    print(res.text)
    return res.json()


def post_s3(document):
    file = {'document': open(document, 'rb')}
    print("Posting to S3")
    res = requests.post(
        url=url_s3,
        files=file
    )

    print(res.text)
    return res.json()


@app.route('/', methods=['GET'])
def index():
    print(request.args)
    if 'subject' in request.args:
        post_rds(
            request.args['subject'],
            request.args['teacher_name'],
            request.args['hours_numbers'],
            request.args['description'])

        return render_template('result.html')

    elif 'document' in request.args:
        post_s3(request.args['document'])
        return render_template('result.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

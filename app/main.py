import pathlib
from os import environ
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

import src.filehandle as fhandle

DBUSER = 'Affenmilchmann'
DBPASS = 'kesha'
DBHOST = 'Affenmilchmann.mysql.pythonanywhere-services.com'
#DBPORT = '1123'
DBNAME = 'hw'
root_dir = str(pathlib.Path().resolve())
survey_data_dir = root_dir + "/survey_data"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{db_type}://{user}:{passwd}@{host}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
  #      port=DBPORT,
        db=DBNAME,
        #db_type = "postgresql+psycopg2",
        db_type = "mysql+pymysql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'foobarbaz'
db = SQLAlchemy(app)

class answers(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    age = db.Column(db.String(100))
    q_1 = db.Column(db.String(200))
    q_2 = db.Column(db.String(200))
    q_3 = db.Column(db.String(200))
    q_4 = db.Column(db.String(200))
    q_5 = db.Column(db.String(200))

    def __init__(self, age, q_1, q_2, q_3, q_4, q_5):
        self.age = age
        self.q_1 = q_1
        self.q_2 = q_2
        self.q_3 = q_3
        self.q_4 = q_4
        self.q_5 = q_5
        
def database_initialization_sequence():
    with app.app_context():
        db.create_all()
        test_rec = answers(
                '20',
                'test1',
                'test2',
                'test3',
                'test4',
                'test5',)
        db.session.add(test_rec)
        db.session.rollback()
        db.session.commit()

@app.route('/', methods=('GET',))
def index():
    return render_template(
        'index.html',
    )
    
@app.route('/form', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        return request.form
    elif request.method == 'GET':
        return render_template(
            'form.html',
            q_data=fhandle.load_questions(survey_data_dir)
        )

@app.route('/stat', methods=('GET',))
def stat():
    return render_template(
        'stat.html',
    )

if __name__ == '__main__':
    database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
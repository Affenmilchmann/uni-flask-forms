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

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))

    def __init__(self, name, city, addr):
        self.name = name
        self.city = city
        self.addr = addr
        
def database_initialization_sequence():
    with app.app_context():
        db.create_all()
        test_rec = students(
                'John Doe',
                'Los Angeles',
                '123 Foobar Ave')
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

if __name__ == '__main__':
    database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
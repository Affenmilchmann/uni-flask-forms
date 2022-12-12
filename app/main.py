import pathlib
from os import environ
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import src.htmltags as htag


DBUSER = 'kesha'
DBPASS = 'kesha'
DBHOST = 'db'
DBPORT = '1123'
DBNAME = 'keshadb'
root_dir = pathlib.Path().resolve()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
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
    
@app.route('/')
def index():
    blist = htag.tag('b', 'unordered list')
    bsublist = htag.tag('b', 'ordered sublist')
    sublist = htag.ol(['i', 'am', 'an', bsublist], style='"color: red"')
    list = htag.ul(['i', 'am', 'an', blist, sublist], style='"color: blue"')
    return render_template(
        'index.html',
        title = 'I am a title',
        content = list,
    )

if __name__ == '__main__':
    database_initialization_sequence()
    app.run(debug=False, host='0.0.0.0')
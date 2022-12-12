from flask_sqlalchemy import SQLAlchemy, MetaData, Table, Column, Integer as dbInt, String as dbStr
from flask import Flask

class KeshaDB(SQLAlchemy):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.kesha_meta = MetaData()
        self.init_tables()
        self.kesha_meta.create_all(engine)
    def init_tables(self):
        kesha = Table(
            'kesha', self.kesha_meta,
            Column('id', dbInt, primary_key = True),
            Column('mood', dbStr)
        )

def check_db(db: SQLAlchemy):
    class kesha(db.Model):
        id = db.Column('kesha_id', db.Integer, primary_key=True)
        mood = db.Column(db.String(100))
        
        def __init__(self, mood) -> None:
            self.mood = mood
            
    
    def database_initialization_sequence():
        db.create_all()
        test_rec = students(
                'John Doe',
                'Los Angeles',
                '123 Foobar Ave')

        db.session.add(test_rec)
        db.session.rollback()
        db.session.commit()
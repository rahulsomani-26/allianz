from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']= 'rahulsomani'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'

db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    profession = db.Column(db.String(50))

    def __init__(self,name,profession):
        self.name = name 
        self.profession = profession

    def __repr__(self):
        return f'Author({self.id} {self.name})'

with app.app_context():
    db.create_all()
    
with app.app_context():
    try:
        db.engine.execute('insert into author values(?,?,?)',(20,'alphabet','musk'))
    except Exception as e:
        print(repr(e))
    result = db.engine.execute('select * from author')
    print(result.fetchall())


if __name__=='__main__':
    app.run(debug=True,port=5400)

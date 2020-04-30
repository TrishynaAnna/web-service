from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from dao.orm.model import Student

app = Flask(__name__)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1998@localhost/Diplom'
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/student', methods=['GET'])
def user():

    result = db.session.query(Student).all()

    return render_template('student.html', users = result)


if __name__ == '__main__':
    app.run()

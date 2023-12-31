from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

connection_string = "postgresql://postgres:123456@localhost:5432/yao"
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>To Do</h1>'

@app.route('/info')
def get_info():
    header = {
        'Access-Control-Allow-Origin': "*"
    }
    data = {
        'name': 'ToDo',
        'dev': 'Yao'
    }
    response = make_response(data)
    response.headers = header
    response.status_code = 200
    return response

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return f'Username: {self.name}'
    
# Call the data seeding function
def seed_db():
    app.app_context().push()
    db.create_all()

    # Data Seeding
    user1 = User(id=1, name='chen')
    user2 = User(id=2, name='lu')
    db.session.add_all([user1, user2])
    db.session.commit()

seed_db()


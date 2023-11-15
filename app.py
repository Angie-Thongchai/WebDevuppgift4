from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///selectdata.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String(50), nullable=False)
    completed= db.Column(db.Integer, default=0)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, content, completed, date_create):
        self.content = content
        self.completed = completed
        self.date_create = date_create

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
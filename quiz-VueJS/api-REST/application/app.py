from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/quiz/api/v1.0/*": {"origins": "http://localhost:3000"}})



import os.path

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            p
        )
    )
    
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "sqlite:///" + mkpath("../application.db")
)

db = SQLAlchemy(app)

#command line interface
@app.cli.command()
def syncdb():
    """create missing tables"""
    db.create_all()
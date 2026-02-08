from flask import Flask
from config import DATABASE_URL;
from routes import *;
from db import db

app = Flask(__name__)

app.register_blueprint(user_routes)
#app.register_blueprint(routine_routes)

# configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = (
    DATABASE_URL
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
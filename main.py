from flask import Flask
from src.database import db
from src.parser.parser import parse

app = Flask(__name__)
# connection string of database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def main():
    parse()


if __name__ == '__main__':
    main()

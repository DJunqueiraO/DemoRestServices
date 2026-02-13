from flask import Flask

from connection.connection import get_database
from src.controller.demo_controller import demo_controller

from sqlalchemy import create_engine
from src.controller.demo_model import Base


def create_tables():
    db = get_database()

    url = (
        f"mysql+pymysql://{db['user']}:{db['password']}"
        f"@{db['host']}:{db['port']}/{db['database']}"
    )

    engine = create_engine(url, echo=True)
    Base.metadata.create_all(engine)


app = Flask(__name__)
app.register_blueprint(demo_controller)


if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=8080)

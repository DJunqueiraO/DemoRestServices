from flask import Flask

from src.adapters.persistence.connection import get_database
from src.adapters.controllers.demo_controller import demo_controller
from src.adapters.controllers.test_controller import test_controller

from sqlalchemy import create_engine
from src.adapters.persistence.sqlalchemy.model.model import Base


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
app.register_blueprint(test_controller)


if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=8080)

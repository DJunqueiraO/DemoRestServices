from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.adapters.persistence.connection import get_database
from src.adapters.persistence.sqlalchemy.repository.demo_repository import DemoRepository
from src.application.services.demo_service import DemoService
from src.domain.entity.demo import Demo

demo_controller = Blueprint('demo_controller', __name__, url_prefix="/demos")

database = get_database()
DATABASE_URL = (
    f"mysql+pymysql://{database['user']}:{database['password']}"
    f"@{database['host']}:{database['port']}/{database['database']}"
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

_demo_service = DemoService(DemoRepository(SessionLocal()))


class DemoController:

    @staticmethod
    @demo_controller.get("/")
    def get_all():
        return jsonify(_demo_service.find_all()), 200

    @staticmethod
    @demo_controller.get("/<int:id_>")
    def get_by_id(id_):
        demo = _demo_service.find_by_id(id_)

        if not demo:
            return jsonify({"error": "not found"}), 404

        return demo, 200

    @staticmethod
    @demo_controller.post("/")
    def create():
        data = request.get_json()

        if not data or "name" not in data:
            return jsonify({"error": "Missing 'name' field"}), 400

        demo = _demo_service.save(Demo.from_dict(data))

        return jsonify(demo), 201

    @staticmethod
    @demo_controller.put("/<int:id_>")
    def update(id_):
        body = request.get_json()
        body["id"] = id_

        if not body:
            return jsonify({"error": "Missing JSON body"}), 400

        demo = _demo_service.update(Demo.from_dict(body))

        if not demo:
            return jsonify({"error": "not found"}), 404

        return jsonify(demo), 200

    @staticmethod
    @demo_controller.delete("/<int:id_>")
    def delete(id_):
        demo = _demo_service.delete_by_id(id_)

        if not demo:
            return jsonify({"error": "not found"}), 404

        return jsonify({"message": "Deleted successfully"}), 200

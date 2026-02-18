from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.adapters.persistence.connection import get_database
from src.adapters.persistence.sqlalchemy.repository.test_repository import TestRepository
from src.application.services.test_service import TestService
from src.domain.entity.test import Test

test_controller = Blueprint('test_controller', __name__, url_prefix="/tests")

database = get_database()
DATABASE_URL = (
    f"mysql+pymysql://{database['user']}:{database['password']}"
    f"@{database['host']}:{database['port']}/{database['database']}"
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

_test_service = TestService(TestRepository(SessionLocal()))


class TestController:

    @staticmethod
    def from_tuple_list(of_name: list[list]) -> list[Test]:
        return list(
            map(lambda test: Test.from_tuple(test), of_name)
        )

    @staticmethod
    @test_controller.get("/")
    def get_all():
        return jsonify(_test_service.find_all()), 200

    @staticmethod
    @test_controller.get("/<int:id_>")
    def get_by_id(id_):
        test = _test_service.find_by_id(id_)

        if not test:
            return jsonify({"error": "Test not found"}), 404

        return test, 200

    @staticmethod
    @test_controller.post("/")
    def create():
        data = request.get_json()

        if not data or "name" not in data:
            return jsonify({"error": "Missing 'name' field"}), 400

        test = _test_service.save(Test.from_dict(data))

        return jsonify(test), 201

    @staticmethod
    @test_controller.put("/<int:id_>")
    def update(id_):
        body = request.get_json()
        body["id"] = id_

        if not body:
            return jsonify({"error": "Missing JSON body"}), 400

        test = Test.from_dict(body)
        _test_service.update(test)

        return jsonify(test), 200

    @staticmethod
    @test_controller.delete("/<int:id_>")
    def delete(id_):
        test = _test_service.delete_by_id(id_)

        if not test:
            return jsonify({"error": "Test not found"}), 404

        return jsonify({"message": "Deleted successfully"}), 200

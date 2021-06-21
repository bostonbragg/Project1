from flask import Flask, request, jsonify
from daos.employee_dao_postgres import EmployeeDAOPostgres
from daos.login_dao_postgres import LoginDAOPostgres
from daos.manager_dao_postgres import ManagerDAOPostgres
from daos.reimbursement_dao_postgres import ReimbursementDAOPostgres
from exceptions.reimbursement_not_found import ReimbursementNotFoundError
from services.employee_service_impl import EmployeeServiceImpl
from services.login_service_impl import LoginServiceImpl
from services.manager_service_impl import ManagerServiceImpl
from services.reimbursement_service_impl import ReimbursementServiceImpl

reimbursement_dao = ReimbursementDAOPostgres()
employee_dao = EmployeeDAOPostgres()
login_dao = LoginDAOPostgres()
manager_dao = ManagerDAOPostgres()
reimbursement_service = ReimbursementServiceImpl(reimbursement_dao)
employee_service = EmployeeServiceImpl(employee_dao)
login_service = LoginServiceImpl(login_dao)
manager_service = ManagerServiceImpl(manager_dao)


def create_routes(app: Flask):
    @app.route("/reimbursements", methods=["POST"])
    def create_reimbursement():
        body = request.json
        reimbursement = reimbursement_service.create_reimbursement(body["employeeID"], float(body["amount"]),
                                                                   body["description"])
        return reimbursement.as_json_dict(), 201

    @app.route("/reimbursements/<r_id>", methods=["GET"])
    def get_reimbursement_by_id(r_id: int):
        reimbursement = reimbursement_service.get_reimbursement_by_id(r_id)
        return reimbursement.as_json_dict(), 200

    @app.route("/employees/reimbursements/<employee_id>", methods=["GET"])
    def get_reimbursements_by_employee(employee_id: int):
        list_of_re = reimbursement_service.get_reimbursements_by_employee(int(employee_id))
        dict_list = [reimbursement.as_json_dict() for reimbursement in list_of_re]
        return jsonify(dict_list), 200

    @app.route("/reimbursements", methods=["GET"])
    def get_all_reimbursements():
        list_of_re = reimbursement_service.get_all_reimbursements()
        dict_list = [reimbursement.as_json_dict() for reimbursement in list_of_re]
        return jsonify(dict_list), 200

    @app.route("/reimbursements/approve/<re_id>", methods=["PATCH"])
    def approve_reimbursement(re_id: int):
        reimbursement = reimbursement_service.get_reimbursement_by_id(int(re_id))
        body = request.json
        message = body["message"]
        try:
            reimbursement = reimbursement_service.approve_reimbursement(reimbursement, message)
        except ReimbursementNotFoundError as e:
            return {"errorMessage": e.message}, 404
        return reimbursement.as_json_dict(), 200

    @app.route("/reimbursements/deny/<re_id>", methods=["PATCH"])
    def deny_reimbursement(re_id: int):
        reimbursement = reimbursement_service.get_reimbursement_by_id(int(re_id))
        body = request.json
        message = body["message"]
        try:
            reimbursement = reimbursement_service.deny_reimbursement(reimbursement, message)
        except ReimbursementNotFoundError as e:
            return {"errorMessage": e.message}, 404
        return reimbursement.as_json_dict(), 200

    @app.route("/employees/<employee_id>", methods=["GET"])
    def get_employee(employee_id: int):
        employee = employee_service.get_employee(int(employee_id))
        return employee.as_json_dict(), 200

    @app.route("/employees", methods=["GET"])
    def get_all_employees():
        employees = employee_service.get_all_employees()
        json_dict = [employee.as_json_dict() for employee in employees]
        return jsonify(json_dict), 200

    @app.route("/login", methods=["POST"])
    def login():
        body = request.json
        username = body["username"]
        password = body["password"]
        login_attempt = login_service.login(username, password)
        return jsonify(login_attempt), 200

    @app.route("/statistics/employees/highest", methods=["GET"])
    def get_highest_total_for_an_employee():
        return jsonify(manager_service.get_highest_total_for_an_employee()), 200

    @app.route("/statistics/status/<status>/highest", methods=["GET"])
    def get_highest_by_status(status: str):
        return jsonify(manager_service.get_highest_by_status(status)), 200

    @app.route("/statistics/status/<status>/mean", methods=["GET"])
    def get_mean_cost_by_status(status: str):
        return jsonify(manager_service.get_mean_by_status(status)), 200

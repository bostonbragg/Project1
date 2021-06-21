from daos.reimbursement_dao_postgres import ReimbursementDAOPostgres
from entities.reimbursement import Reimbursement
from utils.connection_util import connection

try:
    sql = """drop table reimbursement;
    drop table employee;

    create table employee(
        employee_id bigint primary key generated always as identity,
        first_name varchar(50),
        last_name varchar(50),
        is_manager bool,
        username varchar(50) unique,
        pwd varchar(50)
    );
    
    create table reimbursement(
        r_id bigint primary key generated always as identity,
        employee_id bigint,
        amount float,
        description varchar,
        status varchar(50),
        message varchar,
        constraint fk_r_emp foreign key (employee_id) references employee(employee_id)
    );
    insert into employee values (default, 'John', 'Doe', false, 'john.doe', 'password');
    insert into employee values (default, 'Jane', 'Doe', true, 'jane.doe', 'password');
    insert into employee values (default, 'Bigshot', 'CEO', true, 'bigshot.ceo', 'password');
    """

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
except Exception as e:
    print("Database not detected")

dao = ReimbursementDAOPostgres()
test1 = dao.create_reimbursement(1, 100, "Food")
test2 = dao.create_reimbursement(2, 400.50, "Hotel")


def test_create_reimbursement():
    assert test1.amount == 100 and test1.description == "Food" and test1.status == "Pending"


def test_get_reimbursement_by_id():
    r_id = 1
    get_by_id = dao.get_reimbursement_by_id(int(r_id))
    assert test1.description == get_by_id.description


def test_get_reimbursements_by_employee():
    get_by_emp = dao.get_reimbursements_by_employee(1)
    assert get_by_emp[0].description == test1.description


def test_get_all_reimbursements():
    get_all = dao.get_all_reimbursements()
    assert get_all[0].description == test1.description and get_all[1].description == test2.description


def test_approve_reimbursement():
    message = "Seems reasonable"
    approved = dao.approve_reimbursement(test1, message)
    assert approved.status == "Approved" and approved.message == message


def test_deny_reimbursement():
    message = "The Hilton was NOT in the budget, see me in my office ASAP"
    denied = dao.deny_reimbursement(test2, message)
    assert denied.status == "Denied" and denied.message == message

from typing import List
from daos.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from utils.connection_util import connection


class ReimbursementDAOPostgres(ReimbursementDAO):
    def create_reimbursement(self, employee_id: int, amount: float, description: str) -> Reimbursement:
        sql = """insert into reimbursement values (default, %s, %s, %s, 'Pending', '') returning r_id"""
        cursor = connection.cursor()
        cursor.execute(sql, [str(employee_id), str(amount), str(description)])
        connection.commit()
        r_id = cursor.fetchone()[0]
        reimbursement = Reimbursement(r_id, employee_id, amount, description, "Pending", "")
        return reimbursement

    def get_reimbursement_by_id(self, r_id: int) -> Reimbursement:
        sql = """select * from reimbursement where r_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [str(r_id)])
        record = cursor.fetchall()
        for r_parts in record:
            output = Reimbursement(r_parts[0], r_parts[1], r_parts[2], r_parts[3], r_parts[4], r_parts[5])
            return output

    def get_reimbursements_by_employee(self, employee_id: int) -> List[Reimbursement]:
        sql = """select * from reimbursement where employee_id = %s order by r_id"""
        cursor = connection.cursor()
        cursor.execute(sql, [str(employee_id)])
        records = cursor.fetchall()
        r_list = []
        for r_parts in records:
            reimbursement = Reimbursement(r_parts[0], r_parts[1], r_parts[2], r_parts[3], r_parts[4], r_parts[5])
            r_list.append(reimbursement)
        return r_list

    def get_all_reimbursements(self) -> List[Reimbursement]:
        sql = """select * from reimbursement order by r_id"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        r_list = []
        for r_parts in records:
            reimbursement = Reimbursement(r_parts[0], r_parts[1], r_parts[2], r_parts[3], r_parts[4], r_parts[5])
            r_list.append(reimbursement)
        return r_list

    def approve_reimbursement(self, reimbursement: Reimbursement, message: str) -> Reimbursement:
        sql = """update reimbursement set status = 'Approved', message = %s where r_id = %s returning employee_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (str(message), str(reimbursement.r_id)))
        connection.commit()
        return Reimbursement(reimbursement.r_id, reimbursement.employee_id, reimbursement.amount,
                             reimbursement.description, "Approved", message)

    def deny_reimbursement(self, reimbursement: Reimbursement, message: str) -> Reimbursement:
        sql = """update reimbursement set status = 'Denied', message = %s where r_id = %s returning employee_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (str(message), str(reimbursement.r_id)))
        connection.commit()
        return Reimbursement(reimbursement.r_id, reimbursement.employee_id, reimbursement.amount,
                             reimbursement.description, "Denied", message)

from behave.runner import Context
from selenium import webdriver

from poms.approve_or_deny import ApproveOrDeny
from poms.employee_home_page import EmployeeHomePage
from poms.employee_view_reimbursements import EmployeeViewReimbursements
from poms.login_page import LoginPage
from poms.manager_home_page import ManagerHomePage
from poms.statistics import Statistics
from poms.submit_reimbursement_page import SubmitReimbursementPage


def before_all(context: Context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome('drivers\\chromedriver.exe', options=options)

    context.login_page = LoginPage(context.driver)
    context.employee_home_page = EmployeeHomePage(context.driver)
    context.submit_reimbursement = SubmitReimbursementPage(context.driver)
    context.employee_view_reimbursements = EmployeeViewReimbursements(context.driver)
    context.manager_home_page = ManagerHomePage(context.driver)
    context.approve_or_deny = ApproveOrDeny(context.driver)
    context.statistics = Statistics(context.driver)


def after_all(context: Context):
    pass

from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given(u'Employee has logged in and is on the employee home page')
def employee_login(context):
    context.driver.get("file:///C:/Users/bosto/Documents/GitHub/training/Project1/frontend/login.html")
    try:
        context.driver.implicitly_wait(2)
        context.login_page.username()
    except NoSuchElementException:
        context.driver.find_element_by_id("logout").click()
    context.login_page.username().send_keys("john.doe")
    context.login_page.password().send_keys("password")
    context.login_page.login_button().click()
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_id("logout")
    title = context.driver.title
    assert title == "Reimbursement Portal"


@when(u'Employee clicks on Submit a Reimbursement')
def click_submit_reimbursement(context):
    context.employee_home_page.submit_reimbursement().click()


@then(u'Employee is taken to the Submit a Reimbursement form')
def submit_reimbursement_form(context):
    title = context.driver.title
    assert title == "Submit a Reimbursement"


@when(u'Employee inputs the amount for the reimbursement')
def input_amount(context):
    context.submit_reimbursement.amount().send_keys("200")


@when(u'Employee inputs the description for the reimbursement (optional)')
def input_description(context):
    context.submit_reimbursement.description().send_keys("Food")


@then(u'Employee clicks Submit and the form is submitted')
def submit_form(context):
    context.submit_reimbursement.submit().click()
    WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, "messageAfterSubmit")))


@when(u'Employee clicks on View Your Reimbursements')
def click_view_reimbursements(context):
    context.employee_home_page.view_reimbursements().click()
    # context.driver.implicitly_wait(10)
    # context.driver.find_element_by_id("reimbursements")


@then(u'Employee is taken to the View Your Reimbursements page, which displays the reimbursements that Employee has '
      u'submitted')
def view_reimbursements(context):
    title = context.driver.title
    try:
        context.driver.find_element_by_id("reimbursements")
    except NoSuchElementException:
        assert False
    assert title == "View Your Reimbursements"

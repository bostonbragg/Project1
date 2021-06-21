from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given(u'Manager has logged in and is on the manager home page')
def login(context):
    context.driver.get("file:///C:/Users/bosto/Documents/GitHub/training/Project1/frontend/login.html")
    try:
        context.login_page.username()
    except NoSuchElementException:
        context.driver.find_element_by_id("logout").click()
    context.login_page.username().send_keys("bigshot.ceo")
    context.login_page.password().send_keys("password")
    context.login_page.login_button().click()
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_id("logout")
    title = context.driver.title
    assert title == "Reimbursement Portal"


@when(u'Manager clicks on View All Reimbursements')
def click_view_all_reimbursements(context):
    context.manager_home_page.view_all_reimbursements().click()


@then(u'Manager is taken to the View All Reimbursements page, which displays all of the reimbursements that have been '
      u'submitted')
def view_all_reimbursements(context):
    title = context.driver.title
    assert title == "View All Reimbursements"


@when(u'Manager clicks on Approve or Deny Reimbursement')
def approve_or_deny(context):
    context.manager_home_page.approve_or_deny_reimbursement().click()


@then(u'Manager is taken to the Approve or Deny Reimbursement page')
def click_approve_or_deny(context):
    title = context.driver.title
    assert title == "Approve or Deny Reimbursement"


@then(u'Manager selects the reimbursement that they want to approve or deny')
def select_reimbursement(context):
    context.approve_or_deny.reimbursement_id().send_keys("5")


@then(u'Manager chooses whether they want to approve or deny the request')
def select_approve_or_deny(context):
    context.approve_or_deny.approve_or_deny().select_by_value('deny')


@then(u'Manager inputs their message about the reimbursement (optional)')
def input_message(context):
    context.approve_or_deny.message().send_keys("What you've just submitted is one of the most insanely idiotic "
                                                "things I have ever read. At no point in your rambling, incoherent "
                                                "reimbursement request were you even close to anything that could be "
                                                "considered a rational thought. Everyone on this site is now dumber "
                                                "for having listened to it. I award you no reimbursement, and may God "
                                                "have mercy on your soul.")


@then(u'Manager clicks Submit and the form is submitted')
def submit_approve_or_deny(context):
    context.approve_or_deny.submit().click()
    WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, "messageAfterSubmit")))


@when(u'Manager clicks on Statistics')
def click_statistics(context):
    context.manager_home_page.statistics().click()


@then(u'Manager is taken to the Statistics page')
def statistics(context):
    title = context.driver.title
    assert title == "Statistics"


@when(u'Manager clicks on the Highest Total Expenditure Costs for an Employee tab')
def click_highest(context):
    context.statistics.highest_employee().click()


@then(u'Manager is able to view Highest Total Expenditure Costs for an Employee')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, "employees")))


@when(u'Manager clicks on the View Highest Reimbursement by Status tab')
def step_impl(context):
    context.statistics.highest_status().click()


@then(u'Manager is able to view View Highest Reimbursement by Status')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, "reimbursementHTML")))


@when(u'Manager clicks on the View Mean Expenditure Cost by Status tab')
def step_impl(context):
    context.statistics.mean().click()


@then(u'Manager is able to view View Mean Expenditure Cost by Status')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, "amountHTML")))

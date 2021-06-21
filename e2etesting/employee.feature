Feature: Employees should be able to use the Reimbursement Portal

  Scenario: Submit a reimbursement
    Given Employee has logged in and is on the employee home page
    When Employee clicks on Submit a Reimbursement
    Then Employee is taken to the Submit a Reimbursement form
    When Employee inputs the amount for the reimbursement
    When Employee inputs the description for the reimbursement (optional)
    Then Employee clicks Submit and the form is submitted

  Scenario: Get Employee's reimbursements
    Given Employee has logged in and is on the employee home page
    When Employee clicks on View Your Reimbursements
    Then Employee is taken to the View Your Reimbursements page, which displays the reimbursements that Employee has submitted
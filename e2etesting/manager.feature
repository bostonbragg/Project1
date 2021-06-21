Feature: Manager should be able to use the Reimbursement Portal

  Scenario: View all reimbursements
    Given Manager has logged in and is on the manager home page
    When Manager clicks on View All Reimbursements
    Then Manager is taken to the View All Reimbursements page, which displays all of the reimbursements that have been submitted

  Scenario: Approve or deny a reimbursement
    Given Manager has logged in and is on the manager home page
    When Manager clicks on Approve or Deny Reimbursement
    Then Manager is taken to the Approve or Deny Reimbursement page
    Then Manager selects the reimbursement that they want to approve or deny
    Then Manager chooses whether they want to approve or deny the request
    Then Manager inputs their message about the reimbursement (optional)
    Then Manager clicks Submit and the form is submitted

  Scenario: View Highest Total Expenditure Costs for an Employee
    Given Manager has logged in and is on the manager home page
    When Manager clicks on Statistics
    Then Manager is taken to the Statistics page
    When Manager clicks on the Highest Total Expenditure Costs for an Employee tab
    Then Manager is able to view Highest Total Expenditure Costs for an Employee

  Scenario: View Highest Reimbursement by Status
    Given Manager has logged in and is on the manager home page
    When Manager clicks on Statistics
    Then Manager is taken to the Statistics page
    When Manager clicks on the View Highest Reimbursement by Status tab
    Then Manager is able to view View Highest Reimbursement by Status

  Scenario: View Mean Expenditure Cost by Status
    Given Manager has logged in and is on the manager home page
    When Manager clicks on Statistics
    Then Manager is taken to the Statistics page
    When Manager clicks on the View Mean Expenditure Cost by Status tab
    Then Manager is able to view View Mean Expenditure Cost by Status
function redirectToEmployeeHome(){
    window.location.href = "employeehome.html"
}

function redirectToManagerHome(){
    window.location.href = "managerhome.html"
}

function redirectToLoginPage(){
    window.location.href = "login.html"
}

function checkIfLoggedIn(){
    const employeeOrManager = localStorage.getItem("employeeOrManager")
    if(employeeOrManager == "null" || employeeOrManager == undefined){
        redirectToLoginPage()
    }
}

function employeePageOnly(){
    const employeeOrManager = localStorage.getItem("employeeOrManager")
    
    if(employeeOrManager == "Manager"){
        redirectToManagerHome()
    }

    else{
        checkIfLoggedIn()
    }
}

function managerPageOnly(){
    const employeeOrManager = localStorage.getItem("employeeOrManager")
    if(employeeOrManager == "Employee"){
        redirectToEmployeeHome()
    }

    else{
        checkIfLoggedIn()
    }
}

function logout(){
    localStorage.setItem("employeeID", null)
    localStorage.setItem("employeeOrManager", null)
    window.location.href = "login.html"
}

function getEmployeeID(){
    return localStorage.getItem("employeeID")
}

function currencyFormatter(){
    const formatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
    });
    return formatter;
}
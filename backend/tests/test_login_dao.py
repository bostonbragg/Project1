from daos.login_dao_postgres import LoginDAOPostgres

dao = LoginDAOPostgres()


def test_login():
    username = "john.doe"
    password = "password"
    output = dao.login(username, password)
    assert output["responseMessage"] == "Login successful"

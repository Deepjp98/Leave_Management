import pymysql
sql_hostname_localhost = 'localhost'
sql_username_local = 'root'
sql_password_local = 'root'
sql_main_database_local = 'leave_managment'
sql_port_localhost = 3306
def createEmployee(request):
    conn = pymysql.connect(host=sql_hostname_localhost, user=sql_username_local,
                           passwd=sql_password_local, db=sql_main_database_local,
                           port=sql_port_localhost)
    try:
        number = request.json["number"]
        name = request.json["firstName"] +" "+request.json["lastName"]
        query = 'INSERT INTO register(name, email, number, password,user_type) values ("' + name + '","' + request.json["email"] + '","' + str(number) + '","' + request.json[
                    "password"] + '","Employee");'
        cur = conn.cursor()
        status = cur.execute(query)
        conn.commit()
        sql = "SELECT id FROM register ORDER BY id DESC LIMIT 1"
        cur.execute(sql)
        record = cur.fetchone()
        unique_id = 0
        for lastID in record:
            unique_id = lastID

        emp_code = "emp_000"+str(unique_id)
        query = 'INSERT INTO employee(emp_code, emp_name, leave_type,emp_type,user_id) values ("' + emp_code + '","' + name + '","'+ request.json["LeaveType"] + '","Employee","'+str(unique_id)+'");'
        print(query)
        cur = conn.cursor()
        status = cur.execute(query)
        conn.commit()
    except Exception as e:
        print(str(e))
        return {'message': "Something went Wrong", 'Status': 'Success'}

    return {'message': "User created Successfully !!!", 'Status': 'Success'}
import pymysql
sql_hostname_localhost = 'localhost'
sql_username_local = 'root'
sql_password_local = 'root'
sql_main_database_local = 'leave_managment'
sql_port_localhost = 3306

def validateUser(request):
    msg = ""
    status = True
    if 'firstName' not in request.json:
        msg += ', firstname field is missing'
        status = False
    elif 'lastName' not in request.json:
        msg += ',lastname field is missing'
        status = False
    elif 'email' not in request.json:
        msg += ',email field is missing'
        status = False
    elif 'number' not in request.json:
        msg += ',number field is missing'
        status = False
    elif 'LeaveType' not in request.json:
        msg += ',number field is missing'
        status = False
    elif 'password' not in request.json:
        msg += ',number field is missing'
        status = False
    # elif 'repassword' not in request.json:
    #     msg += ',repassword field is missing'
    #     status = False
    else:
        status = True

    return status, msg


def validate(request):
    msg = ""
    status = True
    if 'name' not in request.json:
        msg+=', name field is missing'
        status = False
    elif 'email' not in request.json:
        msg += ',email field is missing'
        status = False
    elif 'number' not in request.json:
        msg += ',number field is missing'
        status = False
    elif 'password' not in request.json:
        msg += ',password field is missing'
        status = False
    # elif 'repassword' not in request.json:
    #     msg += ',repassword field is missing'
    #     status = False
    else:
        status = True

    return  status, msg

def createSuperUSer(request):
    conn = pymysql.connect(host=sql_hostname_localhost, user=sql_username_local,
                           passwd=sql_password_local, db=sql_main_database_local,
                           port=sql_port_localhost)
    try:
        number = request.json["number"]
        query = 'INSERT INTO register(name, email, number, password,user_type) values ("'+request.json["name"]+'","'+request.json["email"]+'","'+str(number)+'","'+request.json["password"]+'","HR");'
        print(query)
        cur = conn.cursor()
        status = cur.execute(query)
        conn.commit()
    except:
        return {'message': "Something went Wrong", 'Status': 'Success'}

    return {'message': "User created Successfully !!!",'Status': 'Success'}
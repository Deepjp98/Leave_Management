import pymysql
sql_hostname_localhost = 'localhost'
sql_username_local = 'root'
sql_password_local = 'root'
sql_main_database_local = '`leave_managment`'
sql_port_localhost = 3306

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
    name = request.json["name"]+" "+request.json["name"]
    query = 'INSERT INTO cities(name, email, password,) number('+request.json["name"]+','+request.json["email"]+','+request.json["number"]+','+request.json["password"]+'); '
    summary_df['master_id'] = [master_id]
    df = pd.read_sql_query(query, conn)
    return "Success"
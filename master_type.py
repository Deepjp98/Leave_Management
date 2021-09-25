import pymysql
sql_hostname_localhost = 'localhost'
sql_username_local = 'root'
sql_password_local = 'root'
sql_main_database_local = 'leave_managment'
sql_port_localhost = 3306
import datetime
def masterData(request):
    conn = pymysql.connect(host=sql_hostname_localhost, user=sql_username_local,
                           passwd=sql_password_local, db=sql_main_database_local,
                           port=sql_port_localhost)
    masterType = request.json['type']
    if masterType  == "AddYear":
        try:
            date_start_date  = datetime.datetime.strptime(request.json["startDate"], '%Y-%m-%d')
            date_end_date = datetime.datetime.strptime(request.json["endDate"], '%Y-%m-%d')
            current_year = str(date_start_date.year)+"-"+str(date_end_date.year)
            query = 'INSERT INTO add_year(start_date, end_date, current_year, year_status) values ("' + request.json["startDate"] + '","' + request.json["endDate"] + '","' + current_year + '","' + request.json["status"] + '");'
            cur = conn.cursor()
            status = cur.execute(query)
            conn.commit()
            return {'message': "Add year successfully", 'Status': 'Success'}
        except Exception as e:
            return {'message': "Something went Wrong", 'Status': 'Success'}
    elif masterType  == "weekoff":
        try:
            query = 'INSERT INTO week_off(week_off_value, week_status) values ("' + request.json["weekOff"] + '","' + request.json["status"] + '");'
            cur = conn.cursor()
            status = cur.execute(query)
            conn.commit()
            return {'message': "Add week-off successfully", 'Status': 'Success'}
        except Exception as e:
            print(str(e))


            return {'message': "Something went Wrong", 'Status': 'Success'}
    elif masterType  == "LeaveType":
        try:

            query = 'INSERT INTO leave_type(leave_type, status) values ("' + request.json["leaveType"] + '","' + request.json["status"] + '");'
            cur = conn.cursor()
            status = cur.execute(query)
            conn.commit()
            return {'message': "Add Leave Type successfully", 'Status': 'Success'}
        except:
            return {'message': "Something went Wrong", 'Status': 'Success'}
    elif masterType  == "EmpType":
        try:
            query = 'INSERT INTO emp_type(emp_type_value, emp_status) values ("' + request.json["empType"] + '","' + request.json["status"] + '");'
            cur = conn.cursor()
            status = cur.execute(query)
            conn.commit()
            return {'message': "Add Employee Type successfully", 'Status': 'Success'}
        except:
            return {'message': "Something went Wrong", 'Status': 'Success'}
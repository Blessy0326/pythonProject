"""Application"""

import datetime as dt
import json
import logging
import mysql.connector
import configday5 as config

X = config.names["host"]
Y = config.names["user"]
Z = config.names["passwd"]
DB = config.names["database"]

logging.basicConfig(
    filename="testfive.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

#Create the connection object
myconn = mysql.connector.connect(host = X, user = Y, passwd = Z, database = DB)

# printing the connection object
print(myconn)

cursor = myconn.cursor()
class Application:
    """Class Application"""

    def validate_age(self,gender,dob):
        """Validate Age function"""
        gender=gender.lower()
        today = dt.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if gender == "male" and age<21:
            return "Invalid"
        elif gender == "female" and age<18:
            return "Invalid"
        else:
            return "Valid"
    def validate_nationality(self,nationality):
        """Validate nationality function"""
        nationality=nationality.lower()
        if nationality in ('indian', 'american'):
            return "Valid"
        else:
            return "Invalid"
    def validate_state(self,state):
        """Validate state function"""
        state = state.lower()
        state = state.replace(" ","")
        states=["andhrapradesh","arunachal pradesh",
                "assam","bihar","chhattisgarh","karnataka",
                "madhya pradesh","odisha","tamilnadu","telangana", "westbengal"]
        if state in states:
            return "Valid"
        else:
            return "Invalid"
    def validate_salary(self,salary):
        """Validate salary function"""
        if salary >= 10000 and salary <= 90000:
            return "Valid"
        else:
            return "Invalid"
    def validate_pan(self,pan):
        """Validate pan number"""
        cursor.execute("select Request_received from request_info "
                       "where  Pan_Number='{}'".format(pan))
        pan_date = cursor.fetchone()
        if pan_date is not None:
            cursor.execute(
                "SELECT DATEDIFF(CURDATE(),Request_received) from request_info"
                " where  Pan_Number='{}'".format(pan))
            no_of_days = cursor.fetchone()
            no_of_days = int(no_of_days[0])
            print(no_of_days)
            if no_of_days < 5:
                return "Invalid"
            else:
                return "Valid"
        else:
            return "Valid"

obj = Application()
FIRST_NAME = input("Enter first name: ")
MIDDLE_NAME = input("Enter middle name: ")
LAST_NAME = input("Enter last name: ")
D_O_B = input("Enter dob YYYY-MM-DD: ")
D_O_B = dt.datetime.strptime(D_O_B, '%Y-%m-%d')
D_O_B = D_O_B.date()
GENDER_NAME = input("Enter gender: ")
RESPONSE_VAL = obj.validate_age(GENDER_NAME,D_O_B)
print(RESPONSE_VAL)
FLAG_VAL = 0
if RESPONSE_VAL != 'Valid':
    REASON_VAL = "Invalid age"
    print(REASON_VAL)
    FLAG_VAL = 1
if FLAG_VAL == 0:
    NATIONALITY_NAME = input("Enter the nalitionality")
    RESPONSE_VAL = obj.validate_nationality(NATIONALITY_NAME)
    print(RESPONSE_VAL)
    if RESPONSE_VAL != 'Valid':
        REASON_VAL = "Invalid nationality"
        print(REASON_VAL)
        FLAG_VAL = 1
else:
    NATIONALITY_NAME = "Invalid"
if FLAG_VAL == 0:
    CURRENT_CITY = input("Enter current city: ")
else:
    CURRENT_CITY = "Invalid"
if FLAG_VAL == 0:
    STATE_NAME = input("Enter State: ")
    RESPONSE_VAL = obj.validate_state(STATE_NAME)
    print(RESPONSE_VAL)
    if RESPONSE_VAL != 'Valid':
        REASON_VAL = "Invalid State"
        print(REASON_VAL)
        FLAG_VAL = 1
else:
    STATE_NAME = "Invalid"

if FLAG_VAL == 0:
    PIN_CODE = input("Enter Pin code: ")
else:
    PIN_CODE = "Invalid"
if FLAG_VAL == 0:
    QUALIFICATION_NAME = input("Enter Qualification: ")
else:
    QUALIFICATION_NAME = "Invalid"
if FLAG_VAL == 0:
    SALARY_OF_PERSON = float(input("Enter Salary: "))
    RESPONSE_VAL = obj.validate_salary(SALARY_OF_PERSON)
    print(RESPONSE_VAL)
    if RESPONSE_VAL != 'Valid':
        REASON_VAL = "Invalid salary"
        print(REASON_VAL)
        FLAG_VAL = 1
else:
    SALARY_OF_PERSON = 0
if FLAG_VAL == 0:
    PAN_NUM = input("Enter pan number: ")
    RESPONSE_VAL = obj.validate_pan(PAN_NUM)
    if RESPONSE_VAL != 'Valid':
        REASON_VAL = "Pan exists"
        FLAG_VAL = 1
    else:
        REASON_VAL = "Success"
else:
    PAN_NUM = "Invalid"

if FLAG_VAL == 0:
    NOW_TIME = dt.datetime.now()
    REASON_VAL = "Success"
    print(RESPONSE_VAL)
else:
    NOW_TIME = dt.datetime.now()

cursor.execute("INSERT INTO request_info(First_name,Middle_name,Last_name,DOB,Gender,"
               "Nationality,Current_city,State,Pin_code,Qualification,Salary,Pan_number,"
               "Request_received)VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',"
               "'{}','{}','{}')".format(FIRST_NAME,MIDDLE_NAME,LAST_NAME,D_O_B,GENDER_NAME,
                NATIONALITY_NAME,CURRENT_CITY,STATE_NAME,PIN_CODE,QUALIFICATION_NAME,
                SALARY_OF_PERSON,PAN_NUM,NOW_TIME))
SQL= "SELECT max(Request_id) FROM request_info"
cursor.execute(SQL)

req_id = cursor.fetchone()
req_id=int(req_id[0])
print(type(req_id))
diction_name = {"Request_id":req_id,"Response":REASON_VAL}
diction_name = json.dumps(diction_name)
logging.info(diction_name)
print(diction_name)
cursor.execute("INSERT INTO response_info(Request_id,response) VALUES"
               " ('{}','{}')".format(req_id, diction_name))

myconn.commit()
import datetime as dt
import json
def Check_eligibity(gender,dob,nationality,state,salary):
    dob= dt.datetime.strptime(dob, '%Y-%m-%d')
    dob=dob.date()
    today = dt.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    flag =0
    nationality = nationality.lower()
    if nationality in ["indian","america"]:
        response = 'Valid'
    else:
        response = 'Invalid nationality'
        flag = 1
    if flag == 0:
        state = state.lower()
        state = state.replace(" ", "")
        states = ["andhrapradesh", "arunachal pradesh",
                  "assam", "bihar", "chhattisgarh", "karnataka",
                  "madhya pradesh", "odisha", "tamilnadu", "telangana", "westbengal"]
        if state in states:
            response = 'Valid'
        else:
            response = "Invalid state"
            flag = 1


    if flag == 0:
        if gender == 'male':
            if age < 21:
                response = 'Invalid age'
                flag = 1
            else:
                response = 'Valid'
        else:
            if age<18:
                response = 'Invalid age'
                flag = 1
            else :
                response = 'Valid'

    if flag == 0:
        salary = int(salary)
        if salary>20000 and salary < 90000:
            response = 'Valid'
        else:
            response = 'Invalid salary'

    diction_name = {"Response": response}
    diction_name = json.dumps(diction_name)
    return diction_name









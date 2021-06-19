#Program to get name,age,gender,salary,state,city
try:
 name=input("Enter the name:")
 age=int(input("enter the age:"))
 gender=input("Enter the gender:")
 salary=int(input("Enter the salary:"))
 state=input("Enter the state")
 city=input("Enter the city")

 print("The entered details:")
 print("Name:",name)
 print("Age:",age)
 print("Gender:",gender)
 print("Salary:",salary)
 print("State:",state)
 print("City:",city)

except ValueError:
   print("Value error occured")
except (TypeError, ZeroDivisionError):
   print("Divided by 0 or type exception occured")
except IOError:
    print("IO exception occured")
except NameError:
    print("Invalid variable")
except:
    print("Some other exception has occured")





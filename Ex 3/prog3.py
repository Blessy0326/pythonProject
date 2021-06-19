import time

try:
 number=2
 while(number>0):
       if number > 1:
          for i in range(2, number):
               if (number % i) == 0:
                  break
          else:
            print(number)
            time.sleep(5)
          number=number+1
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

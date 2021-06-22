import csv
try:
 filename = "file.csv"
 with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        print(line)
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



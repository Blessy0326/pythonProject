#Ascii value of a character
try:
 a=input("Enter the character")
 n=ord(a)
 print(n)
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



#To convert Decimal To bianry,octal,hexadecimal.
try:
 n=int(input("Enter the decimal value:"))
 print(bin(n), " binary.")
 print(oct(n), " octal.")
 print(hex(n), " hexadecimal.")
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


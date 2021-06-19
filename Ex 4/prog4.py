# Python program to find H.C.F of two numbers

# define a function
try:
 def compute_hcf(x, y):

    if x > y:
        n = y
    else:
        n = x
    for i in range(1, n+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


 a = int(input("Enter an Integer: "))
 b = int(input("Enter an Integer: "))
 print("The H.C.F. is", compute_hcf(a,b))
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


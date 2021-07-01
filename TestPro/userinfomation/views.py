from django.shortcuts import render
import datetime as dt
from .models import userdatainfo
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')
def userinfosub(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        middle_name = request.POST["mname"]
        last_name = request.POST["lname"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        nationality = request.POST["nationality"]
        state = request.POST["state"]
        pincode = request.POST["pincode"]
        qualification = request.POST["qualification"]
        salary = request.POST["salary"]
        pannum = request.POST["pannum"]
        requestreceived = dt.datetime.now()

        data = userdatainfo(fname=first_name,mname=middle_name,lname=last_name,dob=dob,gender=gender,nationality=nationality,
                        state=state,pincode=pincode,qualificaton=qualification,salary=salary,pannum=pannum)
        data.save()
        return HttpResponse("<h1>submitted</h1>")
    return render(request, "index.html")




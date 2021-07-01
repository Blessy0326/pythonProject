from django.shortcuts import render
from .models import userdatainfo,responseinfo
from django.http import HttpResponse
from .validation import Check_eligibity
# Create your views here.
def home(request):
    return render(request, 'index.html')
def userinfosub(request):
    if request.method == "POST":
        f_name = request.POST["fn"]
        m_name = request.POST["mn"]
        l_name = request.POST["ln"]
        db = request.POST["d_o_b"]
        g_name = request.POST["gn"]
        n_name = request.POST["nm"]
        s_name = request.POST["sn"]
        pin_name = request.POST["pc"]
        q_name = request.POST["qn"]
        sal_name = request.POST["ss"]
        p_name = request.POST["pn"]


        data = userdatainfo(first_name=f_name,middle_name=m_name,last_name=l_name,dob=db,gender=g_name,nationality=n_name,
                        state=s_name,pincode=pin_name,Qualification=q_name,salary=sal_name,pannum=p_name)
        data.save()
        # return HttpResponse("<h1>submitted</h1>")
        data1 = Check_eligibity(g_name,db,n_name,s_name,sal_name)
        data_2 = responseinfo(response = data1)

        data_2.save()
        return HttpResponse(data1)
    return render(request, "index.html")


from django.shortcuts import render,redirect
from destinyapp.models import reservation,adminlogin
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def packages(request):
    return render(request,'packages.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    if request.method=='POST':
        Name_c=request.POST.get('name')
        EmailId_c=request.POST.get('emailid')
        Guest_c=request.POST.get('guest')
        CheckInDate_c=request.POST.get('checkindate')
        Destination_c=request.POST.get('destination')
        user=reservation(Name=Name_c,EmailId=EmailId_c,Guest=Guest_c,CheckInDate=CheckInDate_c,Destination=Destination_c)
        user.save()
        return redirect('contact')
    return render(request,'contact.html')
def loginadmin(request):
    if request.method=='POST':
        EmailId_a=request.POST.get('emailid')
        Password_a=request.POST.get('password')
        admin_a=adminlogin.objects.all().values()
        print()
        # adminlogin_1={"data":admin_a}
        # print(adminlogin_1['data'])
        if EmailId_a==admin_a[0]['EmailId'] and Password_a==admin_a[0]['Password']:
             admin_model=reservation.objects.all()
             admin1={"data":admin_model}
             return render(request,'admin.html',admin1)
    return render(request,'adminlogin.html')
    
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'ht/homepage.html')

def chk(request):
	return HttpResponse("<script>alert('Hi Good Afternoon') </script><h2>Welcome</h2>")

def homepage(request):
	return render(request,'ht/homepage.html')

def lgn(re):
	return render(re,'ht/login.html')

def reg(rt):
	if rt.method=="POST":
		emailaddress=rt.POST['a']
		pas=rt.POST['b']
		ages=rt.POST['ag']
		return render(rt,'ht/homepage.html',{'info':emailaddress,'info1':pas,'info2':ages})


	return render(rt,'ht/register.html')
def bthm(qw):
	return render(qw,'ht/bthome.html')

def about(req):
	return render(req,'ht/about.html')

def contact(requ):
	return render(requ,'ht/contact.html')
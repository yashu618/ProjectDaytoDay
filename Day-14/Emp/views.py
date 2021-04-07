from django.shortcuts import render,redirect
from Emp.models import UsrRg
from Emp.forms import UsregForm,Userupdate
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def cont(request):
	return render(request,'html/cont.html')

def login(request):
	return render(request,'html/login.html')

def registration(request):
	if request.method=="POST":
		u=request.POST['uname']
		p=request.POST['pd']
		m=request.POST['eml']
		a=request.POST['ag']
		d={'us':u,'em':m,'age':a,'ps':p}

		return render(request,'html/details.html',{'d':d})

	return render(request,'html/register.html')

def crud(request):
	if request.method=="POST":
		un=request.POST['username']
		pas=request.POST['password']
		email=request.POST['email']
		age=request.POST['age']
		data2=UsrRg.objects.all()
		if len(un)!=0:

			data=UsrRg.objects.create(username=un,password=pas,email=email,age=age)

		return render(request,'html/actions.html',{'info':data2})

	data2=UsrRg.objects.all()
	return render(request,'html/actions.html',{'info':data2})

def deletedata(req,st):
	data=UsrRg.objects.get(id=st)
	data.delete()
	return redirect('/cr')

def dform(request):
	if request.method=="POST":
		e=UsregForm(request.POST)
		if e.is_valid():
			e.save()
			data2=UsrRg.objects.all()
			return render(request,'html/user.html',{'info':data2})
	e = UsregForm()
	return render(request,'html/dyform.html',{'tu':e}) 


def showinfo(req):
	data=UsrRg.objects.all()
	return render(req,'html/showdata.html',{'info':data}) 

def infodelete(req,et):
	data=UsrRg.objects.get(id=et)
	if req.method=="POST":
		data.delete()
		return redirect('/showdata') 
	return render(req,'html/userdelete.html',{'sd':data})  

# def edit(request,id):
#     data=UsrRg.objects.get(id=id)
#     if request.method=="POST":
#     	data.username=request.POST['username']
#     	data.email=request.POST['email']
#     	data.age=request.POST['age']
#     	data.password=request.POST['password']
#     	data.save() 
#     	return HttpResponse("Data Saved")
#     return render(request,'html/userupdate.html',{'info':data})	

def userupdate(up,si):
	t=UsrRg.objects.get(id=si)
	if up.method=="POST":
		d=Userupdate(up.POST,instance=t)
		if d.is_valid():
			d.save()
			return redirect('/showdata') 
	d=Userupdate(instance=t)
	return render(up,'html/updateuser.html',{'us':d})







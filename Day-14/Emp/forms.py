from Emp.models import UsrRg
from django import forms 



class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username","required":True,}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email-Id","required":True,}),}

class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Update Username","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Update Email-Id","required":True,}),
         "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update Age","required":True,}),
		}


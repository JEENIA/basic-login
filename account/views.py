from django.shortcuts import render, redirect
from account.forms import RegistrationForm

# Create your views here.
def home(request):
	numbers = [1,2,3,4,5]
	name = 'Jeenia'
	args ={'myName': name, 'numbers': numbers}
	return render(request, 'account/home.html',args)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm()
		args = {'form' : form}
		return render(request, 'account/reg_form.html',args)
	
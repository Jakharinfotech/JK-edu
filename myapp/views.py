from django.shortcuts import render,redirect
from .forms import ManagerSignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,AddressInfo,PersonalInfo
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def index(request):
	return render(request,'myapp/index.html')

def managers(request):
    users = User.objects.all()
    return render(request,'myapp/view_managers.html',{'users':users})



#**********admin panel*******
@login_required
def panel(request):
    
    return render(request,'myapp/home.html')



   



@login_required
def log_out(request):
    logout(request)
    return redirect('myapp:index')



@login_required
def createManager(request):
    form = ManagerSignUpForm(request.POST)
    if request.method == 'POST':
        print("yes")
        if form.is_valid():
     
            user = form.save(commit=False)
            user.save()
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            country = form.cleaned_data.get('country')
            zipcode = form.cleaned_data.get('zipcode')
            personal = PersonalInfo.objects.create(user=user)
            personal.save()
            address = AddressInfo.objects.create(user=user,address=address,city=city,state=state,country=country,zipcode=zipcode)
            address.save()

            print('username')

        
            return render(request,'myapp/home.html')
        else:
            error = "form is not valid"
            return render(request,'myapp/create_manager.html',{'form':form,'error':error})
    form = ManagerSignUpForm()
    return render(request,'myapp/create_manager.html',{'form':form})

"""def panel(request):
    return render(request,'myapp/back/home.html')

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('myapp:index')"""
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from myapp.models import User,User_type
from django import forms

"""class StudentSignUpForm(UserCreationForm):
	city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','dob','city')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user"""

"""user_type = User_type.objects.all()
user_types = [tuple([i,i]) for i in user_type]"""



class ManagerSignUpForm(UserCreationForm):
    
    #user_type = forms.ChoiceField(choices=user_types,label=("user_type"),required=True)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=15)
    state = forms.CharField(max_length=15)
    country = forms.CharField(max_length=20)
    zipcode = forms.CharField(max_length=50)

    #subjects = forms.ChoiceField(choices=subjects)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','mobile','user_type')

    def __init__(self, *args, **kwargs):
        super(ManagerSignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


"""class StudentSignUpForm(UserCreationForm):
    mobile = 
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email')"""


    
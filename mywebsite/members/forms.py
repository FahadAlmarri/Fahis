from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'text-field form-control','placeholder' : 'البريد الإلكتروني'} ))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field','placeholder' : 'الاسم الأول'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field','placeholder' : 'الاسم الأخير'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field','placeholder' : 'اسم المستخدم'}))
    password1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field',"id":"password-field", 'type':'password'}))
    password2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field','type':'password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def init(self, args, **kwargs):
        super(RegisterUserForm, self).init(args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'text-field'
        self.fields['password1'].widget.attrs['class'] = 'text-field'
        self.fields['password1'].widget.attrs['id'] = 'password-field'
        self.fields['password2'].widget.attrs['class'] = 'text-field'


# forms.py

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'text-field',
        'placeholder': 'البريد الإلكتروني',
        'type': 'email',
        'name': 'email'
        }))

class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        label=("كلمة مرور جديدة"),
        widget=forms.PasswordInput(attrs={'placeholder': 'كلمة مرور جديدة', 'class': 'text-field'}),
        
    )
    new_password2 = forms.CharField(
        label=("تأكيد كلمة المرور"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'تأكيد كلمة المرور', 'class': 'text-field'}),
    )

# urls.py


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'text-field form-control','placeholder' : 'البريد الإلكتروني'} ))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field','placeholder' : 'الاسم الأول'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field'}))
    password1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field',"id":"password-field"}))
    password2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'text-field'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def init(self, args, **kwargs):
        super(RegisterUserForm, self).init(args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'text-field'
        self.fields['password1'].widget.attrs['class'] = 'text-field'
        self.fields['password1'].widget.attrs['id'] = 'password-field'
        self.fields['password2'].widget.attrs['class'] = 'text-field'
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


User= get_user_model()

class contactForm(forms.Form):
    name= forms.CharField(max_length= 100, required=False, help_text='max 100 words allowed')
    email= forms.EmailField()
    comment= forms.CharField( widget=forms.Textarea)


# class UserLoginForm(forms.Form):
#     username= forms.CharField(max_length=10)
#     password= forms.CharField(widget= forms.PasswordInput)
#
#     def clean(self, *args, **kwargs):
#         username= self.cleaned_data.get('username')
#         password= self.cleaned_data.get('password')
#
#         if username and password:
#             user=authenticate( username= username, password= password)
#             if not user or not user.check_password(password):
#                 raise forms.ValidationError('Incorrect username or password')
#             #if not user.check_password(password):
#                 #raise forms.ValidationError(' incorrect password')
#         return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget= forms.PasswordInput)

    class Meta:
        model=User
        fields= [
            'username',
            'email'
        ]

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email already exists')
        return email

    def clean_password(self):
        password=self.cleaned_data.get('password')
        confirm_password= self.cleaned_data.get('confirm_password')
        if password and confirm_password != confirm_password:
            raise forms.ValidationError("Password must be same")
        return password

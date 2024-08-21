from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from App_Login.models import UserProfile

class SignUpForm(UserCreationForm):

    # Additional email field added in the UserCreationForm
    email = forms.EmailField(required=True)

    class Meta:
        # Related the model with the User model to have fields accordingly
        model = User
        # the username, password 1 and password2 are coming from the UserCreationForm 
        fields = ('username','email','password1','password2')

class UserProfileChange(UserChangeForm):
    
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password")

    def __init__(self, *args, **kwargs):
        super(UserProfileChange, self).__init__(*args, **kwargs)
        # Remove the help text for the password field
        self.fields['password'].help_text = None

class ProfilePic(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_pic',)

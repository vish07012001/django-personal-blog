from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm,UserProfileChange,ProfilePic
from .models import UserProfile
from .forms import ProfilePic

# Create your views here.
def sign_up(request):
    form = SignUpForm()
    registered =  False
    if request.method == 'POST' :
        # username = request.POST['name']
        # email = request.POST['email']
        # password = request.POST['password']
        # confrim_password = request.POST['confirm_password']
        form = SignUpForm(data =  request.POST)
        if form.is_valid():
            form.save()
            registered =  True

    dict =    {'form': form , 'registered': registered}
    return render(request,'App_Login/signup.html', context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            valid_user_or_not = authenticate(username=username,password=password)
            if valid_user_or_not is not None:
                login(request,valid_user_or_not)
                return HttpResponseRedirect(reverse("index"))
        
    dict = {'form': form}
    return render(request,"App_Login/login.html",context=dict)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("signin"))

@login_required
def profile(request):
    dict = {}
    return render(request,"App_login/profile.html",context=dict)


@login_required
def user_change(request):
    current_user = request.user
    # instance=current_user, the form is pre-populated with the current user's data. 
    # This allows the user to see and potentially modify their existing profile information.
    form = UserProfileChange(instance=current_user) 
    if request.method == "POST":
        # Request.POST reinitializes the UserProfileChange form with the data submitted by the user 
        # instance=current_user argument ensures that the form will update the existing user profile 
        # rather than creating a new one.
        form = UserProfileChange(request.POST, instance = current_user)
        if form.is_valid:
            form.save()
            # form is reinitialized with the updated data to refresh the form with the saved values. 
            # This allows the user to see their changes reflected in the form after submission.
            form = UserProfileChange(instance=current_user)

    dict = {'form': form}
    return render(request,'App_login/change_profile.html',context=dict)

# TO change password
@login_required
def pass_change(request):

    current_user = request.user
    pass_changed = False
    if request.method == "POST":

        form = PasswordChangeForm(current_user, data = request.POST)

        if form.is_valid():
            form.save()
            # Update the session to prevent logging out the user after password change
            update_session_auth_hash(request, form.user)
            pass_changed = True
        
    else:

        form = PasswordChangeForm(current_user)

            
    dict = {'form':form, 'pass_changed': pass_changed}
    return render(request,'App_Login/pass_change.html',context=dict)

@login_required
def add_profile_pic(request):

    # Ensure the UserProfile exists, or create it if it doesn't
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    form = ProfilePic()

    if request.method == "POST":

        form = ProfilePic(request.POST,request.FILES)

        if form.is_valid():
            user_profile.profile_pic = form.cleaned_data['profile_pic']
            user_profile.save()
            return HttpResponseRedirect(reverse("profile"))               

    return render(request,"App_Login/pro_pic_add.html",context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == "POST":
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))
    return render(request,"App_Login/pro_pic_add.html",context={'form':form})

        




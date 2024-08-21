from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.login_page, name='signin'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change_profile/',views.user_change,name='change_profile'),
    path('password/',views.pass_change,name='pass_change'),
    path('changeprofileimage/',views.add_profile_pic,name='add_profile_pic'),
    path('updateprofileimage/',views.change_pro_pic,name='update_profile_pic'),




]
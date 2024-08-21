from django.urls import path
from . import views


urlpatterns = [
    path('',views.BlogList.as_view(),name='blog_list'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<slug:slug>',views.blog_details,name='blog_details'),
    path('liked/<int:pk>',views.liked,name='liked_post'),
    path('unliked/<int:pk>',views.unliked,name='unliked_post'),
    path('my-blog/',views.MyBlogs.as_view(),name='my_blogs'),
    path('edit-blog/<int:pk>',views.UpdateBlog.as_view(),name='edit_blog'), 
]
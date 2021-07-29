from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:page>', views.index, name='index'),
    path('groups', views.groups, name="groups"),
    path("add", views.add, name="add"),
    path("creategroup", views.creategroup, name="creategroup"),
    path("post", views.post, name="post"),
    path("share/<int:share_id>", views.share, name="share"),
    path("good/<int:good_id>", views.good, name="good"),
    #追加
    path('signup/', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]
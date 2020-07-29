from django.urls import path
from . import views
app_name = "Registration"
urlpatterns = [
    path('signup/', views.signup, name="SignUp"),
    path('',views.loginpage, name="Login")
]

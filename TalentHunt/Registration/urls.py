from django.urls import path
from . import views
app_name = "Registration"
urlpatterns = [
    path('', views.signup, name="SignUp"),
    path('signup_validation/', )
]

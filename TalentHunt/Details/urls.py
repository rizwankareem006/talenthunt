from django.urls import path
from . import views
app_name = "Details"
urlpatterns = [
    path('logout/', views.signout, name="Logout"),
    path('skills/', views.skills, name="Skills"),
]
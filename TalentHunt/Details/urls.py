from django.urls import path
from . import views
app_name = "Details"
urlpatterns = [
    path('logout/', views.signout, name="Logout"),
    path('indiskills/', views.indiskills, name="IndividualSkills"),
    path('feed/<int:page>/', views.feed, name="Feed"),
    path('profile/<str:username>', views.profile, name="Profile"),
]
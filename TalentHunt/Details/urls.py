from django.urls import path
from . import views
app_name = "Details"
urlpatterns = [
    path('logout/', views.signout, name="Logout"),
    path('skills/', views.skills, name="Skills"),
    path('feed/<int:page>/', views.feed, name="Feed"),
    path('profile/<str:username>', views.profile, name="Profile"),
    path('profile/update/<str:username>', views.profileupdate, name="ProfileUpdate"),
    path('createTeam/', views.createteam, name="CreateTeam"),
    path('teamprofile/<int:team>', views.teamprofile, name="TeamProfile"),
    path('teamprofile/update/<int:team>', views.teamprofileupdate, name="TeamProfileUpdate"),
]
from django.urls import path
from . import views
app_name = "Details"
urlpatterns = [
    path('logout/', views.signout, name="Logout"),
    path('skills/', views.skills, name="Skills"),
    path('feed/<int:page>/', views.feed, name="Feed"),
    path('profile/<str:username>', views.profile, name="Profile"),
    path('profile/update/<str:username>/', views.profileupdate, name="ProfileUpdate"),
    path('createTeam/', views.createteam, name="CreateTeam"),
    path('teamprofile/<int:team>/', views.teamprofile, name="TeamProfile"),
    path('teamacceptrequest/<int:team>/<str:user>/', views.teamacceptrequest, name="TeamAcceptRequest"),
    path('teamdeclinerequest/<int:team>/<str:user>/', views.teamdeclinerequest, name="TeamDeclineRequest"),
    path('useracceptrequest/<str:user>/<int:team>', views.useracceptrequest, name="UserAcceptRequest"),
    path('userdeclinerequest/<str:user>/<int:team>', views.userdeclinerequest, name="UserDeclineRequest"),
    path('usersendrequest/<int:team>/<str:user>/', views.usersendrequest, name="UserSendRequest"),
    path('teamsendrequest/<int:team>/',views.teamsendrequest, name="TeamSendRequest"),
]
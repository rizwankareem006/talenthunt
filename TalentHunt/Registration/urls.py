from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "Registration"
urlpatterns = [
    path('signup/', views.signup, name="SignUp"),
    path('',views.loginpage, name="Login")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
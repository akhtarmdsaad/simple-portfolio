from django.urls import path
from edu import views
urlpatterns = [
    path("",views.edu,name="skills"),
]

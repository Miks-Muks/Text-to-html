from django.urls import path
from tth import views
urlpatterns = [
    path('', views.convector)
]
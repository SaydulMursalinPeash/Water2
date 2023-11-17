from django.urls import path
from .views import home,GetSensors

urlpatterns = [
    path('',home,name='home_view'),
    path('api/sensors/',GetSensors.as_view(),name='get_all_sensors')
]

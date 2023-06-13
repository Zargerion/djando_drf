from app_in_proj.views import *
from django.urls import path

urlpatterns = [
    path('create_random_data', RandomDataAPIView.as_view(), name='create_random_data'),
    path('сity_population', CityPopulationAPIView.as_view(), name='сity_population'),
    path('test', TestAPIView.as_view(), name='test'),
    path('', Hi.as_view()),
]

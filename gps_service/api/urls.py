from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views



urlpatterns = [
    path('data/list', views.DataList.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('user_params', views.UserParamList.as_view()),
    path('data', views.DataLoad.as_view()),
]
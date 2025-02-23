from django.urls import path
from users import views

urlpatterns = [
    path('registration/', views.registration_api_view.as_view()),
    path('authorization/', views.authorization_api_view.as_view()),
    path('confirm/', views.SmsCode_api_view.as_view()),
]

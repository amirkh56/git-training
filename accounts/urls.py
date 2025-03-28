from django.urls import path
from . import views
# from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    # path('api-token-auth/', auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user', views.UserVIewSet)
urlpatterns += router.urls



# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MzI1MjcwMCwiaWF0IjoxNzQzMTY2MzAwLCJqdGkiOiJhOWRmODQzYmNkMzU0MTFlOTJlNzNkMDk4NjE5YWM2YiIsInVzZXJfaWQiOjF9.hqWuXS5TOvdOSBMsA2DU41wrn2La3WeJUxP15meCSLg",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzMTY2NjAwLCJpYXQiOjE3NDMxNjYzMDAsImp0aSI6IjAxOTA2YzQzMzRhZDRmN2RhNjE5NTM4NjBmYmM0NDM2IiwidXNlcl9pZCI6MX0.MNWOKlrOwuxmfQUyDE7HS-9xjl-PITtyx1NIAg5y0Ho"
# }
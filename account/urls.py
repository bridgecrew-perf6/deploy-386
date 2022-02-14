from django.urls import URLPattern, path
from .views import RegistrationView, ActivationView, LogoutView,\
    ForgotPasswordView, CompleteResetPasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:email>/<str:code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('forgot_password/<str:email>/', ForgotPasswordView().as_view()),
    path('complete_recovery', CompleteResetPasswordView().as_view()),
]

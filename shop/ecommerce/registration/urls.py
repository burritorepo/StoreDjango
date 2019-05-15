from django.urls import path
from .views import MySignUpView
from django.contrib.auth.views import (PasswordChangeView, LoginView, LogoutView, PasswordChangeDoneView, 
PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import reverse_lazy

app_name = 'registration'

urlpatterns = [
    path('sign_up/', MySignUpView.as_view(), name='sign_up'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('registration:password_change_done')), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uibd64>/<tokens>/', PasswordResetConfirmView.as_view(success_url='/account/reset/done/'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
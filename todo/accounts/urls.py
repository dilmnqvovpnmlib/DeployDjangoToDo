from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),  # 登録
    path('', views.AccountsView.as_view(), name='accounts'),
]

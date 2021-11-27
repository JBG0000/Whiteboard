from django.urls import path

from joinapp.views import JoinView

app_name = "joinapp"

urlpatterns = [
    path('join/', JoinView.as_view(), name='join')
]
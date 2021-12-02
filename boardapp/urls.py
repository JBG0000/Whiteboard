from django.urls import path

from boardapp.views import BoardCreateView, BoardUpdateView, BoardDetailView, BoardDeleteView, \
    NoticeListView, DataListView, BoardListView

app_name = "boardapp"

urlpatterns = [
    path('create/', BoardCreateView.as_view(), name='create'),
    path('update/<int:pk>', BoardUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', BoardDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BoardDeleteView.as_view(), name='delete'),

    path('list/notice/', NoticeListView.as_view(), name='notice'),
    path('list/data/', DataListView.as_view(), name='data'),
    path('list/board/', BoardListView.as_view(), name='board'),
]

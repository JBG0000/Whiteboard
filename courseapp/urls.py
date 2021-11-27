from django.urls import path

from courseapp.views import CourseListView, CourseCreateView, CourseDetailView, CourseUpdateView, CourseDeleteView, \
    CourseSignupView

app_name = 'courseapp'

urlpatterns = [
    path('list/', CourseListView.as_view(), name='list'),
    path('signup/', CourseSignupView.as_view(), name='signup'),

    path('create/', CourseCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete'),
]
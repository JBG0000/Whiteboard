from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from courseapp.decorators import course_ownership_required
from courseapp.forms import CourseCreationForm
from courseapp.models import Course


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseCreationForm
    template_name = 'courseapp/create.html'

    def form_valid(self, form):
        temp_course = form.save(commit=False)
        temp_course.writer = self.request.user
        temp_course.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('courseapp:detail', kwargs={'pk': self.object.pk})


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'target_course'
    template_name = 'courseapp/detail.html'

    def get_context_data(self, **kwargs):
        course = self.object
        user = self.request.user


@method_decorator(course_ownership_required, 'get')
@method_decorator(course_ownership_required, 'post')
class CourseUpdateView(UpdateView):
    model = Course
    context_object_name = 'target_project'
    form_class = CourseCreationForm
    template_name = 'courseapp/update.html'

    def get_success_url(self):
        return reverse('courseapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(course_ownership_required, 'get')
@method_decorator(course_ownership_required, 'post')
class CourseDeleteView(DeleteView):
    model = Course
    context_object_name = 'target_course'
    success_url = reverse_lazy('courseapp:list')
    template_name = 'courseapp/delete.html'

@method_decorator(login_required, 'get')
class CourseListView(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'courseapp/list.html'

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from boardapp.decorators import board_ownership_required, LoginRequired
from boardapp.forms import BoardCreationForm
from boardapp.models import Board
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from courseapp.models import Course


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class BoardCreateView(CreateView):
    model = Board
    form_class = BoardCreationForm
    template_name = 'boardapp/create.html'

    def form_valid(self, form): #form 등록
        temp_course = Course.objects.get(pk=self.request.POST['course_pk'])  # hidden으로 보내준 course_pk

        temp_board = form.save(commit=False)
        temp_board.writer = self.request.user
        temp_board.course = temp_course
        temp_board.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        target_user = self.request.user
        target_course_pk =self.request.GET.get('course_pk')
        return super(BoardCreateView, self).get_context_data(target_user=target_user, target_course_pk=target_course_pk, **kwargs)

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})


class BoardDetailView(LoginRequired, DetailView, FormMixin):
    login_url = '/accounts/login/'
    model = Board   #여기에 writer 정보가 있을건데,,,
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'boardapp/detail.html'

    def get_context_data(self, **kwargs):   #특정정보를 따올 때
        comment_list = Comment.objects.filter(board=self.object.pk).order_by('-created_at')
        # if user.is_authenticated: #로그인 했는가?
        # join = Join.objects.filter(user=user, project=project)
        # object_list = Post.object(project=self.get_object())
        return super(BoardDetailView, self).get_context_data(comment_list=comment_list, **kwargs)


@method_decorator(board_ownership_required, 'get')
@method_decorator(board_ownership_required, 'post')
class BoardUpdateView(UpdateView):
    model = Board
    context_object_name = 'target_post'
    form_class = BoardCreationForm
    template_name = 'boardapp/update.html'

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(board_ownership_required, 'get')
@method_decorator(board_ownership_required, 'post')
class BoardDeleteView(DeleteView):
    model = Board
    context_object_name = 'target_post'
    success_url = reverse_lazy('boardapp:list')
    template_name = 'boardapp/delete.html'

class BasicListView(LoginRequired, ListView):
    login_url = '/accounts/login/'
    model = Board
    context_object_name = 'post_list'
    ordering = ['-id']

#공지사항 게시판
class NoticeListView(BasicListView):
    template_name = 'boardapp/notice.html'


    def get_queryset(self):
        notice_list = Board.objects.filter(type='notice', course__pk=self.request.GET.get('course_pk')).order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(notice_list, 4)
        queryset = paginator.get_page(page)

        return queryset

    def get_context_data(self, **kwargs):   #따오기
        target_course = get_object_or_404(Course, pk=self.request.GET.get('course_pk'))

        return super(NoticeListView, self).get_context_data(target_course=target_course, **kwargs)

#강의자료 게시판
class DataListView(BasicListView):
    template_name = 'boardapp/data.html'

    def get_queryset(self):
        data_list = Board.objects.filter(type='data', course__pk=self.request.GET.get('course_pk')).order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(data_list, 4)
        queryset = paginator.get_page(page)

        return queryset

    def get_context_data(self, **kwargs):   #따오기
        target_course = get_object_or_404(Course, pk=self.request.GET.get('course_pk'))

        return super(DataListView, self).get_context_data(target_course=target_course, **kwargs)

#토론 게시판
class BoardListView(BasicListView):
    template_name = 'boardapp/board.html'

    def get_queryset(self):
        board_list = Board.objects.filter(type='board', course__pk=self.request.GET.get('course_pk')).order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(board_list, 4)
        queryset = paginator.get_page(page)

        return queryset

    def get_context_data(self, **kwargs):   #따오기
        target_course = get_object_or_404(Course, pk=self.request.GET.get('course_pk'))

        return super(BoardListView, self).get_context_data(target_course=target_course, **kwargs)
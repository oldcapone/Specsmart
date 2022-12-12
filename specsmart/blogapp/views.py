from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Post, Tag
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView,TemplateView
from django.views.generic.base import ContextMixin


class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Теги'
        return context

class MainView(ListView, NameContextMixin):
    model = Post
    template_name = 'blogapp/index.html'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Post.objects.all()

class AboutDetailView(TemplateView):
    template_name = 'blogapp/about.html'

class ElementsView(TemplateView):
    template_name = 'blogapp/elements.html'


class BlogsView(TemplateView):
    template_name = 'blogapp/blog.html'

class BlogView(TemplateView):
    template_name = 'blogapp/single-blog.html'

class PostView(DetailView, NameContextMixin):
    model = Post
    template_name = 'blogapp/post.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.post_id = kwargs['id']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Post, id=self.post_id)

# noinspection PyUnusedLocal
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из форы
            name_1 = form.cleaned_data['name_1']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            tel_1 = form.cleaned_data['tel_1']
            # отпарвка письма
            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                'ivanov.planeta@gmail.com', #от кого
                [email], #кому
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'blogapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'blogapp/contact.html', context={'form': form})


# CRUD CREATE, READ (LIST, DETAIL), UPDATE, DELETE
# список тегов
class TagListView(ListView, NameContextMixin):
    model = Tag
    template_name = 'blogapp/tag_list.html'
    context_object_name = 'Теги'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Tag.objects.all()

# детальная информация
# детальная информация
class TagDetailView(DetailView, NameContextMixin):
    model = Tag
    template_name = 'blogapp/tag_detail.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.tag_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Tag, pk=self.tag_id)

# создание тега
class TagCreateView(CreateView, NameContextMixin):
    # form_class =
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'

    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        return super().form_valid(form)


# class TagUpdataView(UpdateView):
#     fields = '__all__'
#     model = Tag
#     success_url = reverse_lazy('blog:tag_list')
#     template_name = 'blogapp/tag_create.html'
#
#
# class TagDeleteView(DeleteView):
#     template_name = 'blogapp/tag_delete_confirm.html'
#     model = Tag
#     success_url = reverse_lazy('blog:tag_list')

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Tag
from .forms import ContactForm
from django.core.mail import send_mail



def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})

def about(request):
    return render(request, 'blogapp/about.html')

def elements(request):
    return render(request, 'blogapp/elements.html')

def blogs(request):
    return render(request, 'blogapp/blog.html')

def blog(request):
    return render(request, 'blogapp/single-blog.html')

def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post})


# noinspection PyUnusedLocal
def contact_form(request):
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

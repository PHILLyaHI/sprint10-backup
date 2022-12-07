from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from projectapp.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from projectapp.forms import *
from django.views import View


class HomeView(ListView):
    model = Video
    template_name = "projectapp/index.html"

class VideoDetailView(DetailView):
    model = Video
    template_name = "projectapp/video_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Video, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class AddVideoView(CreateView):
    model = Video
    template_name = "projectapp/add_video.html"
    fields = ["title", "preview", "video", "user", "description"]


def LikeView(request, pk):
    video = get_object_or_404(Video, id=request.POST.get('video_id'))
    video.likes.add(request.user)
    return HttpResponseRedirect(reverse('video-detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    template_name = "projectapp/add_comment.html"
    fields = "__all__"

def search_videos(request):
    if request.method == "POST":
        searched = request.POST['searched']
        videos = Video.objects.filter(title__contains=searched)
        return render(request, 'projectapp/search_videos.html', {"searched": searched, "videos": videos})
    else:
        return render(request, 'projectapp/search_videos.html', {})


class UserListView(ListView):
    model = Profile
    template_name = "projectapp/user_list.html"


class EmailView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "projectapp/email.html", {})

    def post(self, request, *args, **kwargs):
        email = Email(
            client_name=request.POST['client_name'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        email.save()

        send_mail( 
            subject=email.client_name,  # имя клиента и дата записи будут в теме для удобства
            message=email.message,  # сообщение с кратким описанием проблемы
            from_email='phillippapetenok@gmail.com', # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=[]  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )

        return redirect('index')


class VideoDeleteView(DeleteView):
    model = Video
    template_name = "projectapp/delete_video.html"
    success_url = "index"



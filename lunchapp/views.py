from urllib.parse import urlparse, parse_qs
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse, HttpResponseBadRequest
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from lunchapp.forms import CommentForm, RegistrationForm, TopicForm
from lunchapp.models import Comment, Topic


class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        topics = Topic.objects.all()
        topic_form = TopicForm()
        return render(request, 'lunch_index.html', {
            'topics': topics,
            'topic_form': topic_form
        })


class Login(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'form': AuthenticationForm})

    def post(self, request, **kwargs):
        response = HttpResponseForbidden("Wrong username or password")
        if request.user.is_authenticated():
            return HttpResponseRedirect('lunch_index', status=200)

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', '')
            )
            if user is not None:
                login(request, user)
                return redirect('lunch_index')
        return response


class Register(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('lunch_index')
        return render(request, 'register.html', {'form': RegistrationForm()})

    def post(self, request, **kwargs):
        if request.user.is_authenticated():
            return redirect('lunch_index')
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('lunch_index')
        return render(request, 'register.html', {'form': form})


class TopicList(TemplateView):
    def get(self, request, *args, **kwargs):
        # TODO Incomplete.
        return redirect('lunch_index')

    def post(self, request, **kwargs):
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('/lunch/topics/' + str(topic.id))
        return redirect('lunch_index')


class TopicDetail(TemplateView):
    def get(self, request, *args, topic_id=0, **kwargs):
        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return redirect('lunch_index')

        comments = Comment.objects.filter(topic=topic_id)
        edit_topic_form = TopicForm()
        comment_form = CommentForm()
        delete_redirect_url = reverse('lunch_index')
        return render(request, 'topic.html', {
            'comments': comments,
            'comment_form': comment_form,
            'edit_topic_form': edit_topic_form,
            'topic': topic,
            'delete_redirect_url': delete_redirect_url
        })

    def post(self, request, topic_id=0):
        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return redirect('lunch_index')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            return redirect('/lunch/topics/' + str(topic.id))

        return render(request, 'topic.html', {
            'comments': Comment.objects.filter(topic=topic_id),
            'comment_form': comment_form,
            'topic': topic
        })

    def delete(self, request, *args, topic_id=0, **kwargs):
        try:
            topic = Topic.objects.get(id=topic_id, author=request.user)
        except Topic.DoesNotExist:
            return HttpResponseBadRequest('No such topic found.')
        topic.delete()
        # Return 200.
        return HttpResponse()


class TopicEdit(TemplateView):
    def post(self, request, *args, topic_id=0, **kwargs):
        try:
            topic = Topic.objects.get(id=topic_id, author=request.user)
        except Topic.DoesNotExist:
            return HttpResponseBadRequest('No such topic found.')
        name = request.POST.get('name', None)
        text = request.POST.get('text', None)
        if name is not None:
            topic.name = name
            topic.edited = True
        if text is not None:
            topic.text = text
            topic.edited = True
        topic.save()

        # Return 200.
        return HttpResponse()


class CommentDetail(TemplateView):
    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, topic_id=0, comment_id=0, **kwargs):
        try:
            comment = Comment.objects.get(id=comment_id, author=request.user)
        except Comment.DoesNotExist:
            return redirect('/lunch/topics/' + str(topic_id))

        comment.text = None
        comment.author = None
        comment.save()
        return redirect('/lunch/topics/' + str(topic_id))

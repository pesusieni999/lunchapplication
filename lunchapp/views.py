from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm, PasswordChangeForm

from lunchapp.forms import CommentForm, RegistrationForm, TopicForm
from lunchapp.models import Comment, Topic
from social_django.models import UserSocialAuth


__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Ohsiha Project"
__credits__ = ["Ville Myllynen"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ville Myllynen"
__email__ = "ville.myllynen@student.tut.fi"
__status__ = "Development"


class IndexPage(TemplateView):
    """
    Main page of Lunch application.
    """
    def get(self, request, **kwargs):
        topics = Topic.objects.all()
        topic_form = TopicForm()
        return render(request, 'lunch_index.html', {
            'topics': topics,
            'topic_form': topic_form
        })


class Login(TemplateView):
    """
    Login page for the system.
    """
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
    """
    Registration page for the system.
    """
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


class Topics(TemplateView):
    """
    Topic page. Get single topic, create a new topic or delete existing topic.
    """
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

    def post(self, request, topic_id):
        name = request.POST.get('name', None)
        text = request.POST.get('text', None)

        try:
            topic = Topic.objects.get(id=topic_id)
            topic.name = name
            topic.text = text
        except Topic.DoesNotExist:
            if topic_id != "0":
                return HttpResponseRedirect('lunch_index')
            topic = Topic(author=request.user, name=name, text=text)
        topic.save()
        return HttpResponseRedirect(reverse('topics', kwargs={'topic_id': topic.id}))

    def delete(self, request, *args, topic_id=0, **kwargs):
        try:
            topic = Topic.objects.get(id=topic_id, author=request.user)
        except Topic.DoesNotExist:
            return HttpResponseBadRequest('No such topic found.')
        topic.delete()
        # Return 200.
        return HttpResponse()


class Comments(TemplateView):
    """
    View for creating, updating and deleting comments.
    Note: Deleting leaves the entry but author and text is cleared.
    """
    def post(self, request, topic_id=0, comment_id=0):
        text = request.POST.get('text', None)
        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return HttpResponseRedirect('lunch_index')

        try:
            comment = Comment.objects.get(id=comment_id, topic=topic)
            comment.text = text
        except Comment.DoesNotExist:
            if comment_id != "0":
                return HttpResponseRedirect('lunch_index')
            comment = Comment(author=request.user, text=text, topic=topic)
        comment.save()
        return HttpResponseRedirect(reverse('topics', kwargs={'topic_id': topic.id}))

    def delete(self, request, *args, topic_id=0, comment_id=0, **kwargs):
        try:
            comment = Comment.objects.get(id=comment_id, author=request.user)
        except Comment.DoesNotExist:
            return redirect(reverse('topics', kwargs={'topic_id': topic_id}))
        comment.text = None
        comment.author = None
        comment.save()
        return HttpResponse()


class Settings(TemplateView):
    """
    Settings page. Here user can link/unlink Github accounts to local account.
    """
    def get(self, request, *args, **kwargs):
        user = request.user

        try:
            github_login = user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            github_login = None

        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        return render(request, 'settings.html', {
            'github_login': github_login,
            'can_disconnect': can_disconnect
        })


class Password(TemplateView):
    """
    Password management page. Change password.
    """
    def get(self, request, *args, **kwargs):
        if request.user.has_usable_password():
            password_form = PasswordChangeForm
        else:
            password_form = AdminPasswordChangeForm

        form = password_form(request.user)
        return render(request, 'password.html', {'form': form})

    def post(self, request):
        if request.user.has_usable_password():
            password_form = PasswordChangeForm
        else:
            password_form = AdminPasswordChangeForm

        form = password_form(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            pass
            # messages.error(request, 'Please correct the error below.')
        return render(request, 'password.html', {'form': form})

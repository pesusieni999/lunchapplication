from django.conf.urls import url, include
from django.contrib.auth.views import logout


from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='lunch_index'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': 'lunch_index'}, name='logout'),
    url(r'^oauth/', include('social_django.urls'), name='social'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.Topics.as_view(), name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/(?P<comment_id>\d+)/$', views.Comments.as_view(), name='comments'),
]

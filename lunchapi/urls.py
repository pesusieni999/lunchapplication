from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from lunchapi import views

urlpatterns = [
    url(r'^topics/$', views.TopicList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view()),
    url(r'^topics/(?P<topic_id>[0-9]+)/comments/$', views.CommentList.as_view()),
    url(
        r'^topics/(?P<topic_id>[0-9]+)/comments/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view()
    ),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='lunch_index'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': 'lunch_index'}, name='logout'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^topics/$', views.TopicList.as_view(), name='topic_list'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.TopicDetail.as_view(), name='topic_details'),
    # This is a workaround URL for Django not working well with AJAX PUT.
    url(r'^topics/(?P<topic_id>\d+)/edit/$', views.TopicEdit.as_view(), name='topic_edit'),
]

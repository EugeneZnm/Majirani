from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

url(r'^profile_edit/$', views.profile_edit,name='edit_profile'),

url(r'^profile/$', views.profile, name='profile'),

url(r'^search/$', views.search_biz, name='search_biz'),

url(r'^newhood/$', views.create_hood, name='newhood'),

url(r'^neighbourhood/(?P<neighbourhood_id>\d+)', views.neighbourhood, name='neighbourhood'),

url(r'^newbiz/$', views.createbiz, name='newbiz'),

url(r'updatebiz/(\d+)$', views.updatebiz, name='updatebiz'),

url(r'^post/$', views.create_post, name='post'),

url(r'^comment/(\d+)', views.comm, name='comment'),

# url(r'^hood/$', views.currenthood, name="currenthood"),

url(r'^enterhood/(?P<neighbourhood_id>\d+)$', views.enter_hood, name='enterhood'),
#
url(r'^exithood/(?P<neighbourhood_id>\d+)$', views.exit_hood, name='exithood'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
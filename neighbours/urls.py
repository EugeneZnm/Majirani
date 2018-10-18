from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

url(r'^profile_edit/', views.profile_edit,name='edit_profile'),

url(r'^profile/', views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
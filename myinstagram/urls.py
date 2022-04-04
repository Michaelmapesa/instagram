from django.urls import path, include,re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$',views.home_images,name='homePage'),
    path('^search/', views.search_users, name='search_users'),
    re_path(r'^image/(\d+)',views.image,name ='image'),
    path('^users/', views.user_list, name = 'user_list'),
    path('^new/image$', views.new_image, name='new_image'),
    path('^edit/profile$', views.edit_profile, name='edit_profile'),
    path('^profile/(?P<username>[0-9]+)$', views.individual_profile_page, name='individual_profile_page'),
    path('^myprofile/$', views.myprofile, name='myprofile'),

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

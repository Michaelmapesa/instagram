from django.urls import path, include,re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$',views.home_images,name='homePage'),
    re_path(r'^search/', views.search_users, name='search_users'),
    re_path(r'^image/(\d+)',views.image,name ='image'),
    re_path(r'^users/', views.user_list, name = 'user_list'),
    re_path(r'^new/image$', views.new_image, name='new_image'),
    re_path(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    re_path(r'^profile/(?P<username>[0-9]+)$', views.individual_profile_page, name='individual_profile_page'),
    # url(r'^comment/(?P<image_id>\d+)', views.add_review, name='add_review'),
    re_path(r'^myprofile/$', views.myprofile, name='myprofile'),
    # url(r'^(?P<image_id>\d+)/preference/(?P<userpreference>\d+)/$', views.postpreference, name='postpreference'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

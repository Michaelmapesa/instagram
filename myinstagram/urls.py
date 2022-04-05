from django.urls import path, include,re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    re_path(r'^$',views.home_images,name='homePage'),
    re_path(r"login",views.login_request,name="login"),
    re_path(r"register",views.register_request,name="register"),
    re_path(r'^search/', views.search_users, name='search_users'),
    re_path(r'^image/(\d+)',views.image,name ='image'),
    re_path(r'^users/', views.user_list, name = 'user_list'),
    re_path(r'^new/image$', views.new_image, name='new_image'),
    re_path(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    re_path(r'^profile/(?P<username>[0-9]+)$', views.individual_profile_page, name='individual_profile_page'),
    re_path(r'^myprofile/$', views.myprofile, name='myprofile'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    # path("logout", views.logout_request, name= "logout"),

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

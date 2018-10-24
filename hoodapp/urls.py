from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$',views.index,name = 'index'),
#   url(r'^signup/$', views.signup, name='signup'),
#   url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#       views.activate, name='activate'),
  url(r'^search/',views.search_business, name='search_business'),
  url(r'^add_hood/$', views.add_hood, name='add_hood'),
  url(r'^join/(\d+)',views.join_hood,name='join_hood'),
  url(r'^home/$',views.home,name = 'home'),
  url(r'^edit_hood/(\d+)',views.edit_hood,name="edit_hood"),
  url(r'^leave_hood/(\d+)',views.leave_hood,name = 'leave_hood'),
  url(r'^add_business/$',views.add_business,name= 'add_business'),
  url(r'^businesses/$',views.added_businesses,name= 'added_businesses'),
  url(r'^edit_business/(\d+)',views.edit_business,name = 'edit_business'),
  url(r'^profile/$',views.profile,name = 'profile'),
  url(r'^update_profile/$',views.update_profile,name= 'update_profile'),
  url(r'^add_post/$',views.add_post,name = 'add_post'),
  url(r'^posts/$',views.posts,name = 'posts'),
  url(r'^edit_post/(\d+)',views.edit_post,name = 'edit_post'),
  url(r'searched/', views.search_results, name='search_results'),
  url(r'^delete_hood/(\d+)',views.delete_hood,name = 'delete_hood'),
  url(r'^delete_post/(\d+)',views.delete_post,name = 'delete_post'),
  url(r'^delete_business/(\d+)',views.delete_business,name = 'delete_business'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
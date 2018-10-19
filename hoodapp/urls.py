from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$',views.index,name = 'index'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
      views.activate, name='activate'),
  url(r'^search/',views.search_business, name='search_business'),
  url(r'^add_hood/$', views.add_hood, name='add_hood'),
  url(r'^edit_hood/(\d+)',views.edit_hood,name="edit_hood"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
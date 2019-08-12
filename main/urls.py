from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$',views.view_projects,name='view_projects'),
    url(r'^download/media/(?P<file_name>.+)$',views.download,name='download'),
    url(r'^index/$',views.index, name='webfront')
]
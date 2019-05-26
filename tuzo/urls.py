from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^project/$', views.upload_project, name='upload_project'),
    url(r'^rate/(\d+)',views.vote_project,name = 'rate'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
     url(r'^post/(?P<project_id>[0-9]+)/review_design/$',
        views.rate_design, name='rate_design'),
    url(r'^post/(?P<project_id>[0-9]+)/review_usability/$',
        views.rate_usability, name='rate_usability'),
    url(r'^post/(?P<project_id>[0-9]+)/review_content/$',
        views.rate_content, name='rate_content'),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.ProfileDescription.as_view()),
     url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view())
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
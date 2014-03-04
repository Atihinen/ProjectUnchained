from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from project_unchained import settings

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_unchained.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^accounts/register/', include('register.urls', namespace="register")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += patterns('gui.views',
    url(r'^$', 'index', name="index"),
)

urlpatterns += staticfiles_urlpatterns()

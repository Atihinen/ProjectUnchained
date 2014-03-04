from django.conf.urls import patterns, url

from register import views
from company import views as company_views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'^user/username/(?P<username>\w+)/*', views.is_username_in_use, name="check_username"),
    url(r'^user/email/(?P<email>[^/]+)/*', views.is_email_in_use, name="check_email"),
    url(r'^company/name/(?P<company_name>\w+)/*', company_views.is_company_name_in_use, name="check_company_name"),
)
from django.conf.urls import patterns, url

from gui import views

urlpatterns = patterns(
    '',
    url(r'^$', views.gui, name="index"),
)
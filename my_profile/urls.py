from django.conf.urls import *
from django.views.generic import TemplateView

from my_profile.views import ProfileView

urlpatterns = patterns('my_profile.views',
	url(r'^$', LoginView.as_view(), name='log_in'),
	url(r'^callback/$', TemplateView.as_view(template_name='callback.html'))
)
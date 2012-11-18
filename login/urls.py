from django.conf.urls import *
from django.views.generic import TemplateView

from login.views import LoginView

urlpatterns = patterns('rate_the_randoms.views',
	url(r'^$', LoginView.as_view(), name='log_in'),
	url(r'^callback/$', TemplateView.as_view(template_name='callback.html'))

)
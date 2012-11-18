from django.views.generic import TemplateView
from login.utils import JSONResponseOnDemandMixin
from django.views.decorators.csrf import csrf_exempt                                          
from django.utils.decorators import method_decorator


class LoginView(TemplateView, JSONResponseOnDemandMixin):
	template_name='login/log_in.html'

	@method_decorator(csrf_exempt)
	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		context['header'] = 'Log In to 500px!'

		return context
	@method_decorator(csrf_exempt)
	def put(self, request, **kwargs):
		if request.body:
			return self.render_json_response({'success': True})
		return self.render_json_response({'success': True}) 

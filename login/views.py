from django.views.generic import TemplateView
from utils.json_response import JSONResponseOnDemandMixin

class LoginView(TemplateView, JSONResponseOnDemandMixin):
	template_name='login/log_in.html'

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		context['header'] = 'Log In to 500px!'

		return context

	def put(self, request, **kwargs):
		if request.body:
			return self.render_json_response({'success': True})
		return self.render_json_response({'success': True}) 

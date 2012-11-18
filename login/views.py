from django.views.generic import TemplateView

class LoginView(TemplateView):
	template_name='login/log_in.html'

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		context['header'] = 'Log In to 500px!'

		return context

	def put(self, request, **kwargs):
		if request.body:
			pass
		pass
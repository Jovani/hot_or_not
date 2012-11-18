from project_utils.json_encoder import JSONEncoder
from django.http import HttpResponse, HttpResponseNotFound

class JsonResponse(HttpResponse):
    def __init__(self, data):
        content = JSONEncoder().encode(data)
        # NOTE: An attempt to use mimetype='application/json; charset=UTF-8'
        #       failed in Internet Explorer (error code: c00ce56e)
        super(JsonResponse, self).__init__(content=content, mimetype='application/javascript')

class JSONResponseMixin(object):
    """
    Mixin to use with class-based views that provides an extra render_json_response function.
    """
    content_type = 'application/json'

    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        " Construct an HttpResponse object "
        return HttpResponse(content, content_type=self.content_type, **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        return JsonResponse(context)

class JSONResponseOnDemandMixin(object):
    """
    Mixin to use with class-based views that provides an extra 
    render_json_response function.
    """
    content_type = 'application/json'

    def render_json_response(self, context):
        return HttpResponse(JsonResponse(context), content_type=self.content_type)


from django.http import HttpResponseForbidden
from django.template.response import TemplateResponse


class CustomMiddleware:
    def __init__(self, get_response):
        """
        __init__(self, get_response): Called once when the server starts.
          It takes a callable get_response that returns the response object.
        """
        print(f"__init__ called.........")
        self.get_response = get_response
        self.config = self.load_config()

    def load_config(self):
        print(f"Loading configs......")
        # Simulate loading configuration from a file or database
        return {"setting": "value"}

    def __call__(self, request):
        """
        __call__(self, request): Called for each request.
          It processes the request and returns the response.
        """
        print(f"__call__ called........")
        print(f"Request path: {request.path}")
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        process_view(self, request, view_func, view_args, view_kwargs):
        Called just before calling the view.
        """
        print(f"Process_view function......")
        if not request.user.is_authenticated and view_func.__name__ == 'restricted_view':
            return HttpResponseForbidden("You are not authorized to access this page.")

    def process_exception(self, request, exception):
        """
        process_exception(self, request, exception):
        Called when a view raises an exception.
        """
        self.logger.error(f"Exception occurred: {exception}", exc_info=True)

    def process_template_response(self, request, response):
        """
        process_template_response(self, request, response):
        Called if the view returns a TemplateResponse.
        """
        if isinstance(response, TemplateResponse):
            # Add extra context data if the response is a TemplateResponse
            response.context_data['extra_data'] = 'Additional Context Data'
        return response

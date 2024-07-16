from django.http import HttpResponseBadRequest

class CheckHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for a custom header "X-Custom-Header"
        if 'X-Custom-Header' not in request.headers:
            return HttpResponseBadRequest("Missing X-Custom-Header")

        response = self.get_response(request)

        return response
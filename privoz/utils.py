class DisableCSRFCheck:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/graphql/':  # replace 'your_endpoint' with your actual endpoint
            setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response

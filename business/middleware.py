from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticatedUsersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and trying to access the login route
        if request.user.is_authenticated and (request.path == reverse('business:login') or request.path == reverse('business:signup')):
            # Redirect authenticated users to the homepage
            return redirect(reverse('business:homepage'))

        # Continue with the request/response cycle
        response = self.get_response(request)
        return response
from django.shortcuts import redirect
from django.views.generic import View


class Index(View):
    redirect_url = 'account:profile'

    def get(self, request, *args, **kwargs):
        return redirect(self.redirect_url)

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views.generic import View
from account.models import Album, User

from account.forms import (
    UserSignInForm,
    UserSignUpForm,
)


class SignIn(View):
    template_name = 'account/auth/signin.html'
    redirect_url = 'account:profile'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        form = UserSignInForm()

        return render(request=request, template_name=self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        form = UserSignInForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(self.redirect_url)
            else:
                messages.error(request, _('Invalid username or password.'))
        else:
            messages.error(request, _('Invalid username or password.'))

        return render(request=request, template_name=self.template_name, context={'form': form})


class SignUp(View):
    template_name = 'account/auth/signup.html'
    redirect_url = 'account:signin'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        form = UserSignUpForm()

        return render(request=request, template_name=self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        form = UserSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, _('You can Sign In now!'))

            return redirect(self.redirect_url)

        return render(request=request, template_name=self.template_name, context={'form': form})


class Profile(LoginRequiredMixin, View):
    template_name = 'account/account/profile.html'
    login_url = '/account/'
    redirect_url = 'account:profile'

    def get(self, request, *args, **kwargs):
        user = request.user

        if kwargs and kwargs.get('id'):
            try:
                user = User.objects.get(id=kwargs.get('id'))
            except User.DoesNotExist:
                return redirect(self.redirect_url)

        return render(request=request, template_name=self.template_name, context={'user': user})


class Albums(LoginRequiredMixin, View):
    template_name = 'account/photos/albums.html'
    login_url = '/account/'
    redirect_url = 'account:albums'

    def get(self, request, *args, **kwargs):
        author = request.user

        if kwargs and kwargs.get('user_id'):
            try:
                author = User.objects.get(id=kwargs.get('user_id'))
            except User.DoesNotExist:
                return redirect(self.redirect_url)

        albums = Album.objects.filter(author_id=author.pk)

        paginator = Paginator(albums, 10)
        page = request.GET.get('page')
        paged_albums = paginator.get_page(page)

        return render(request=request, template_name=self.template_name, context={'albums': paged_albums})

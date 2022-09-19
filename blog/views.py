from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views.generic import View

from blog.models import Post


class Feed(LoginRequiredMixin, View):
    template_name = 'blog/feed.html'
    login_url = '/account/'
    redirect_url = 'account:profile'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        paginator = Paginator(posts, 10)
        page = request.GET.get('page')
        paged_posts = paginator.get_page(page)

        return render(request=request, template_name=self.template_name, context={'posts': paged_posts})

from django.contrib.auth.views import LogoutView as Logout
from django.urls import path

from account.views import Profile, SignIn, SignUp


app_name = 'account'


urlpatterns = [
    path('', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/<int:id>/', Profile.as_view(), name='profile_int'),
    path('logout/', Logout.as_view(template_name='account/auth/logout.html'), name='logout')
]

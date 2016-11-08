from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
import debug_toolbar
from bfrs import views

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views


def home_view_selection_view(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    else:
        return redirect('login')


def admin_view_selection_view(request):
    if request.user.is_superuser:
        return admin.site.index(request)
    elif request.user.is_authenticated():
        return redirect('dashboard')
    else:
        return redirect('login')


urlpatterns = [
#    url(r'^login/$', 'django.contrib.auth.views.login', name='login',
#        kwargs={'template_name': 'login.html'}),
#    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout',
#        kwargs={'template_name': 'logged_out.html'}),

    # Authentication URLs
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    #url(r'^login/$', auth_views.login),
    url('^', include('django.contrib.auth.urls')),

    url(r'^$', home_view_selection_view, name='home'),
    url(r'^main/', login_required(views.BushfireView.as_view()), name='dashboard'),
    url(r'^admin/$', admin_view_selection_view),
    #url(r'^$', views.BushfireView.as_view(), name='home'),
    url(r'^bfrs/', include('bfrs.urls', namespace='bushfire')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),

    # api
    #url(r'^api/', include(api_urls, namespace='api')),

    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]

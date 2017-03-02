
from django.conf.urls import include, url
from django.contrib import admin
from indianstockideas import views
from django.contrib.auth .views import login
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='home'),
    url(r'^featured/$', login_required(views.FeaturedView.as_view()), name='featured'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^indianstockideas/', include('indianstockideas.urls')),
    url(r'^login/$',login, {'template_name': 'indianstockideas/login.html'},name = 'django.contrib.auth.views.login'),
    url(r'^admin/', admin.site.urls),
]
admin.site.site_header = 'IndianStockIdeas'
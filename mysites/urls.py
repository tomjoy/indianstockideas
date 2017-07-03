
from django.conf.urls import include, url
from django.contrib import admin
from indianstockideas import views
from django.contrib.auth .views import login
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='home'),
    url(r'^screenerdata/$', login_required(views.ScreenerView.as_view()), name='screener'),
    url(r'^nsedata/$', login_required(views.NseDataView.as_view()), name='nse'),
    url(r'^recommended/$', login_required(views.AllDataView.as_view()), name='alldata'),
    url(r'^analysis/$', login_required(views.AnalysisView.as_view()), name='analysisData'),
    url(r'^publish/(?P<symbol>.+)$', login_required(views.PublishView.as_view()), name='publishView'),
    url(r'^unpublish/(?P<symbol>.+)$', login_required(views.UnPublishView.as_view()), name='unPublishView'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^indianstockideas/', include('indianstockideas.urls')),
    url(r'^login/$',login, {'template_name': 'indianstockideas/login.html'},name = 'django.contrib.auth.views.login'),
    url(r'^admin/', admin.site.urls),
]
admin.site.site_header = 'IndianStockIdeas'
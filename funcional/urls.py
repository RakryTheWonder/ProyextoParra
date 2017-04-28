from django.conf.urls import patterns, url 
from django.contrib.auth.decorators import login_required
from .views import Bienvenida

urlpatterns = patterns('',

	url(r'^$',login_required(Bienvenida.as_view()), name="bienvenida"),

)
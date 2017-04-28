from django.conf.urls import patterns, url
from seguridad.views import Login
from django.contrib.auth.views import logout
 
urlpatterns = patterns('',
    url(r'^$', Login.as_view(), name="login"),    
    url(r'^salir$', logout, name="salir", kwargs={'next_page': '/'}), 
        
)
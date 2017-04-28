from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'proyecto1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('seguridad.urls',namespace='seguridad')),
    url(r'^funcional/', include('funcional.urls', namespace='funcional')),

]

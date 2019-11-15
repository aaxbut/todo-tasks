from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'config.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/auth/', include('rest_auth.urls')),
    url(
        r'^api/v1/to-do/',
        include(
            'apps.tasks.urls',
        ),
    ),
]

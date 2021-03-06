from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    "",
    # Examples:
    # url(r'^$', 'mir.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^$", "mir.extractor.views.home", name="/audioclip"),
)

urlpatterns += staticfiles_urlpatterns()

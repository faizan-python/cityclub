from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'club.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'core.views.index', name='core_index'),
    url(r'^league-table/$', 'core.views.league_table', name='league-table'),
    url(r'^fixture-result/$', 'core.views.fixture_result', name='fixture-result'),
    url(r'^team/$', 'core.views.team', name='team'),
    url(r'^news/(?P<news_id>\d+)/$', 'core.views.news', name='news'),
    url(r'^defender/$', 'core.views.defender', name='defender'),
    url(r'^midfielder/$', 'core.views.midfielder', name='midfielder'),
    url(r'^striker/$', 'core.views.striker', name='striker'),
    url(r'^contact-us/$', 'core.views.contact_us', name='contact-us'),
    url(r'^user/(?P<user_id>\d+)/$', 'core.views.user_detail', name='user_details'),
    url(r'^gallery/$', 'core.views.gallery', name='gallery'),
    url(r'^news-all/$', 'core.views.news_all', name='news-all'),
    url(r'^admin/', include(admin.site.urls)),
 )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^club/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

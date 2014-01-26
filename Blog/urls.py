from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^Blog/', include('Blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # App URLs
    url(r'^home/', 'Homemade.views.home', name='home'),
    url(r'^posts/(?P<post_id>(\d+))', 'Homemade.views.posts', name='posts_by_id'),
    url(r'^posts/', 'Homemade.views.posts', name='posts'),
    url(r'^add_post/', 'Homemade.views.add_post', name='add_post'),
    url(r'^add_tags/', 'Homemade.views.add_tags', name='add_tags'),
    url(r'^edit_page/(?P<page_id>(\d+))', 'Homemade.views.edit_page', name='edit_page'),
    url(r'^edit_page/', 'Homemade.views.edit_page', name='add_page'),
    url(r'^view_page/(?P<page_id>(\d+))', 'Homemade.views.view_page', name='view_page'),
    url(r'^$', 'Homemade.views.home', name='home')
)

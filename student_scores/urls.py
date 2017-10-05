from django.conf.urls import include, url
from django.contrib import admin
from django.utils.translation import ugettext_lazy

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_profile/', include('user_profile.urls')),
    url(r'^scores/', include('scores.urls')),

]

admin.site.site_header = 'Student Score Management System'
admin.site.site_title = ugettext_lazy('Score Admin')
admin.site.index_title = ugettext_lazy('Operation Management')

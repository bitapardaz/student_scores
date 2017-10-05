from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^get_score/$',views.get_score),
    #url(r'^get_course_details/$',views.get_course_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)

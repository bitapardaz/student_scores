from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^students/get_student_detail/$',views.get_student_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

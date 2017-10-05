from django.contrib import admin

from models import StudentProfile, UserType, UserUserType
# Register your models here.
admin.site.register(UserType)
admin.site.register(UserUserType)
admin.site.register(StudentProfile)

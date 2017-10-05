from rest_framework import serializers
from models import StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):


    def get_first_name(self,obj):
        return obj.user.first_name

    def get_last_name(self,obj):
        return obj.user.last_name

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = StudentProfile
        fields = ('student_number','first_name','last_name')

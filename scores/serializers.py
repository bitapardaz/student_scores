from rest_framework import serializers
from models import StudentCourseScore
from models import Course

from user_profile.serializers import StudentProfileSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = ('title','code','description','image',)

class StudentCourseScoreSerializer(serializers.ModelSerializer):

    def get_student_first_name(self,obj):
        return obj.student.first_name

    def get_student_last_name(self,obj):
        return obj.student.last_name

    def get_course_title(self,obj):
        return obj.course.title

    def get_course_code(self,obj):
        return obj.course.code

    def get_course_description(self,obj):
        return obj.course.description

    def get_course_image(self,obj):
        return obj.course.image.url

    student_first_name = serializers.SerializerMethodField()
    student_last_name = serializers.SerializerMethodField()
    course_title = serializers.SerializerMethodField()
    course_code = serializers.SerializerMethodField()
    course_description = serializers.SerializerMethodField()
    course_image = serializers.SerializerMethodField()

    class Meta:
        model = StudentCourseScore
        fields = ('score', 'valid_until','student_first_name','student_last_name','course_title','course_code','course_description','course_image',)

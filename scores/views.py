from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import StudentCourseScoreSerializer
from models import StudentCourseScore
from user_profile.models import StudentProfile

@api_view(['POST'])
def get_score(request):

    output = {}

    student_number = request.data.get('student_number')
    student = StudentProfile.objects.get(student_number=student_number).user

    student_course_scores = StudentCourseScore.objects.filter(student=student)
    serializer = StudentCourseScoreSerializer(student_course_scores,many=True)
#    output{'scores'} = serializer.data

    return Response(serializer.data)

@api_view(['GET'])
def get_course_details(request):
    return Response("output:1")

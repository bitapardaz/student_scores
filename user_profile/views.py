from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import StudentProfile

# Create your views here.
@api_view(['POST'])
def get_student_detail(request):

    student_number = request.data.get('student_number')

    print student_number
    output = {}

    try:

        profile = StudentProfile.objects.get(student_number=student_number)

        output['first_name'] = profile.user.first_name
        output['last_name'] = profile.user.last_name
        output['state'] = "0"

    except StudentProfile.DoesNotExist:

        output['state'] = "1"
        output['error_msg'] = "student_number_not_found"

    return Response(output)

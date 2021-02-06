from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from .serializers import *


@api_view(['GET','POST'])
def faculty(request):
    if request.method == 'GET':
        faculty = Faculty.objects.all().filter(status='active')
        serializer = FacultySerializer(faculty, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def faculty_detail(request, pk):

    try:
        faculty = Faculty.objects.get(pk=pk)
    except Faculty.DoesNotExist:
        return Response({'message: Faculty does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def faculty_delete(request, pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
    except Faculty.DoesNotExist:
        return Response({'message: Faculty does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        faculty.status = 'inactive'
        faculty.deleted_date = datetime.now()
        faculty.save()
        return Response({'Faculty deleted'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def students_section(request, pk):
    StudentList= []
    try:
        enr_sec = Enroll_Sect.objects.get(pk=pk)
    except Enroll_Sect.DoesNotExist:
        return Response({'Section doesnt exist'}, status=status.HTTP_404_NOT_FOUND)

    for i in enr_sec:
        enroll = Enrollment.objects.get(pk=i.enrrollment_fk_id)
        if enroll.type == 'S':
            student = Person.objects.get(pk= enroll.person_fk_id)
            StudentList.append(student.name + ' '+ status.lastname)
    return Response(StudentList)




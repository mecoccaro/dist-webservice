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

# School
@api_view(['GET','POST'])
def school(request):
    if request.method == 'GET':
        school = School.objects.all().filter(status='active')
        serializer = SchoolSerializer(school, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def school_detail(request, pk):

    try:
        school = School.objects.get(pk=pk)
    except School.DoesNotExist:
        return Response({'message: School does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def school_delete(request, pk):
    try:
        school = School.objects.get(pk=pk)
    except School.DoesNotExist:
        return Response({'message: School does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        school.status = 'inactive'
        school.deleted_date = datetime.now()
        school.save()
        return Response({'School deleted'}, status=status.HTTP_200_OK)

# Section
@api_view(['GET','POST'])
def section(request):
    if request.method == 'GET':
        section = Section.objects.all().filter(status='active')
        serializer = SectionSerializer(section, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def section_detail(request, pk):

    try:
        section = Section.objects.get(pk=pk)
    except Section.DoesNotExist:
        return Response({'message: Section does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SectionSerializer(section)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def section_delete(request, pk):
    try:
        section = Section.objects.get(pk=pk)
    except Section.DoesNotExist:
        return Response({'message: Section does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        section.status = 'inactive'
        section.deleted_date = datetime.now()
        section.save()
        return Response({'Section deleted'}, status=status.HTTP_200_OK)

#Persons

@api_view(['GET','POST'])
def person(request):
    if request.method == 'GET':
        person = Person.objects.all().filter(status='active')
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def person_detail(request, pk):

    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'message: Person does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(section)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def person_delete(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'message: Person does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        person.status = 'inactive'
        person.deleted_date = datetime.now()
        person.save()
        return Response({'Person deleted'}, status=status.HTTP_200_OK)

#Asignar seccion a una persona
@api_view(['GET','POST'])
def enrollment(request):
    if request.method == 'GET':
        enrollment = Enrollment.objects.all().filter(status='active')
        serializer = EnrollmentSerializer(enrollment, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def enrollment_delete(request, pk):
    try:
        enrollment = Enrollment.objects.get(pk=pk)
    except Enrollment.DoesNotExist:
        return Response({'message: Enrollment does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        enrollment.status = 'inactive'
        enrollment.deleted_date = datetime.now()
        enrollment.save()
        return Response({'Enrollment deleted'}, status=status.HTTP_200_OK)
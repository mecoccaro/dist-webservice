from rest_framework import serializers, fields
from .models import *

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('name',
                  'description')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('status',
                  'name',
                  'description'
                  'faculty')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('status',
                  'name',
                  'description'
                  'uc',
                  'semester',
                  'type',
                  'ht',
                  'hp',
                  'hl',
                  'school')


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('status',
                  'type',)


class EnrollSectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll_Sect
        fields = ('enrollment',
                  'section')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('status',
                  'cedula',
                  'first_name',
                  'last_name',
                  'enrollment')

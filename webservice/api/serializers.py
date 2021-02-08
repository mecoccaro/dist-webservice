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
        fields = ('name',
                  'description',
                  'faculty_fk')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('name',
                  'description',
                  'uc',
                  'semester',
                  'type',
                  'ht',
                  'hp',
                  'hl',
                  'school_fk')


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('type',
                  'person_fk'  )


class EnrollSectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll_Sect
        fields = ('enrollment_fk',
                  'section_fk')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('cedula',
                  'first_name',
                  'last_name')

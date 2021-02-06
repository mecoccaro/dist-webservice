from rest_framework import serializers, fields
from .models import *

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('name',
                  'description')

class FacultyDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('description',)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('status',
                  'name',
                  'description'
                  'faculty')

class SchoolDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('status',)

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

class SectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('status',)

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('status',
                  'type',)

class EnrollmentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('status',)

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

class PersonDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('status',)

from django.conf.urls import url
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from . import views

schema_view = get_swagger_view(title='WebService Distributed')


urlpatterns = [
    url('documentation/', schema_view),

    #Faculty
    url('faculty/', views.faculty),
    url('faculty-details/(?P<pk>[0-9]+)$', views.faculty_detail),
    url('faculty-delete/(?P<pk>[0-9]+)$', views.faculty_delete),

    #Student section
    url('student_section/(?P<pk>[0-9]+)$', views.students_section),

    #School
    url('school/', views.school),
    url('school-details/(?P<pk>[0-9]+)$', views.school_detail),
    url('school-delete/(?P<pk>[0-9]+)$', views.school_delete),

    #Section
    url('section/', views.section),
    url('section-details/(?P<pk>[0-9]+)$', views.section_detail),
    url('section-delete/(?P<pk>[0-9]+)$', views.section_delete),

    #Person
    url('person/', views.person),
    url('person-details/(?P<pk>[0-9]+)$', views.person_detail),
    url('person-delete/(?P<pk>[0-9]+)$', views.person_delete),

    #Enrollment
    url('enrollment/', views.enrollment),
    url('enrollment-delete/(?P<pk>[0-9]+)$', views.enrollment_delete)
]
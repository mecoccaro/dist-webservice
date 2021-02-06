from django.conf.urls import url
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from . import views

schema_view = get_swagger_view(title='WebService Distributed')


urlpatterns = [
    url('documentation/', schema_view),
    url('faculty/', views.faculty),
    url('faculty-details/(?P<pk>[0-9]+)$', views.faculty_detail),
    url('faculty-delete/(?P<pk>[0-9]+)$', views.faculty_delete),
    url('student_section/(?P<pk>[0-9]+)$', views.students_section)
]
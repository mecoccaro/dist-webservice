from django.conf.urls import url
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='WebService Distributed')


urlpatterns = [
    url('documentation/$', schema_view)
]
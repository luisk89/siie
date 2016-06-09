from django.conf.urls import patterns, include, url
from reportes.views import calificacion_extracurricular

urlpatterns = patterns('',
    (r'^calificacion_extracurricular/', calificacion_extracurricular.as_view()),
)
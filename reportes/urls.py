from django.conf.urls import patterns, include, url
from wkhtmltopdf.views import PDFTemplateView
from reportes.views import Boleta_Semestral_To_PDF, Calificacion_por_Materia_to_PDF

urlpatterns = patterns('',
    (r'^pdf/final/(?P<materia_id>\d+)/(?P<plan_id>\d+)/(?P<grupo_id>\d+)', Calificacion_por_Materia_to_PDF.get_data_load),
    (r'^pdf/boleta/(?P<alumno_id>\d+)/$', Boleta_Semestral_To_PDF.get_data_load),


)
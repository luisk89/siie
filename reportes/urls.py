from django.conf.urls import patterns, include, url
from wkhtmltopdf.views import PDFTemplateView
from reportes.views import Boleta_Semestral_To_PDF, Calificacion_por_Materia_to_PDF, Inscripcion_To_PDF,CriteriosView, \
    Reinscripcion_To_PDF

urlpatterns = patterns('',
                       url(r'^pdf/criteva/(?P<model>\w+)/$', CriteriosView.as_view(), name='evafinal'),
                       url(r'^pdf/evafinal/$', Calificacion_por_Materia_to_PDF.as_view(), name='reporte-evafinal'),

                       url(r'^pdf/critboleta/(?P<model>\w+)/$', CriteriosView.as_view(), name='boletaciclo'),
                       url(r'^pdf/boleta/$', Boleta_Semestral_To_PDF.as_view(), name='reporte-boletaciclo'),

                       url(r'^pdf/inscripcion/(?P<model>\w+)/$', CriteriosView.as_view(), name='inscripcion'),
                        url(r'^pdf/repinscrip/(?P<pk>[0-9]+)/$', Inscripcion_To_PDF.as_view(), name='reporte-inscripcion'),

                        url(r'^pdf/reins/(?P<model>\w+)/$', CriteriosView.as_view(), name='reinscripcion'),
                       url(r'^pdf/reinscriprep/(?P<pk>[0-9]+)/$', Reinscripcion_To_PDF.as_view(), name='reporte-reinscripcion'),

                       )

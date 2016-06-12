from django.conf.urls import patterns, include, url
from wkhtmltopdf.views import PDFTemplateView
from reportes.views import MyPDFView

urlpatterns = patterns('',
    (r'^reportes/pdf/', MyPDFView.as_view()),

)
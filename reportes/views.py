from django.utils import timezone
import datetime
import json
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView
from wkhtmltopdf.views import PDFTemplateResponse
from academica.models import Alumnos, Grupos, Calificaciones, Materias, PlanEstudio, Carreras, CicloSemestral
from reportes.forms import InscripcionReporteForm


class CriteriosView(TemplateView):

    def get_context_data(self, **kwargs):
        cxt = super(CriteriosView, self).get_context_data(**kwargs)
        cxt = {'carreras': Carreras.objects.all(), 'materias': Materias.objects.all(), 'grupos': Grupos.objects.all(),
               'semestres': CicloSemestral.objects.all()}
        print('id' + self.kwargs['model'])
        return cxt

    def get_template_names(self):
        model = self.kwargs['model']
        self.model = model
        if model == "boleta":
            self.template_name = "reportes/%s_form.html" % model
        if model == "evafinal":
            self.template_name = "reportes/%s_form.html" % model
        if model=='inscripcion':
            self.template_name="reportes/%s_form.html" % model
        if model=='reinscripcion':
            self.template_name="reportes/%s_form.html" % model
        return self.template_name

class Calificacion_por_Materia_to_PDF(TemplateView):
    template_name = 'reportes/reporte_evafinal_form.html'


class Boleta_Semestral_To_PDF(TemplateView):
    template_name = 'reportes/reporte_boleta_form.html'


class Inscripcion_To_PDF(DetailView):
    template_name = 'reportes/reporte_inscripcion.html'
    form_class = InscripcionReporteForm
    model = Alumnos

    def get_context_data(self, **kwargs):
        cxt = super(Inscripcion_To_PDF, self).get_context_data(**kwargs)
        hoy = datetime.datetime.now()
        hoy = hoy.strftime('%Y-%m-%d')
        alumno=Alumnos.objects.get(id=self.kwargs['pk'])
        fecha_ins=alumno.alta_date_created.strftime('%Y-%m-%d')
        cxt = {'hoy': hoy,'fecha_insc':fecha_ins,'object':alumno}

        return cxt

class Reinscripcion_To_PDF(DetailView):
    template_name = 'reportes/reporte_reinscripcion.html'
    form_class = InscripcionReporteForm
    model = Alumnos

    def get_context_data(self, **kwargs):
        cxt = super(Reinscripcion_To_PDF, self).get_context_data(**kwargs)
        hoy = datetime.datetime.now()
        hoy = hoy.strftime('%Y-%m-%d')
        alumno=Alumnos.objects.get(id=self.kwargs['pk'])
        fecha_ins=alumno.alta_date_created.strftime('%Y-%m-%d')
        cxt = {'hoy': hoy,'fecha_insc':fecha_ins,'object':alumno}

        return cxt
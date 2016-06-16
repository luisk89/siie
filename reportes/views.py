from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import View, TemplateView
from wkhtmltopdf.views import PDFTemplateResponse
from academica.models import Alumnos, Grupos, Calificaciones, Materias, PlanEstudio


class Calificacion_por_Materia_to_PDF(TemplateView):
    template_name='reportes/Reporte_Calificacion_Final.html'
    context= {'title': 'Hello World!'}

    def get_data_load(request, materia_id,plan_id,grupo_id):
        materia=Materias.objects.get(id=materia_id)
        plan=PlanEstudio.objects.get(id=plan_id)
        semestre=materia.semestre
        grupo=Grupos.objects.get(id=grupo_id)
        ciclo='15-16'

        if Calificaciones.objects.filter(materia=materia).exists():
            list=Calificaciones.objects.filter(materia=materia)
        else:
            list=[]
        return render_to_response('reportes/Reporte_Calificacion_Final.html',
                                  {'listado': list, 'materia': materia,'plan': plan,'semestre': semestre,'grupo': grupo,'ciclo': ciclo,})

class Boleta_Semestral_To_PDF(TemplateView):
    template_name='reportes/Reporte_boleta_semestral.html'
    context= {'title': 'Hello World!'}
    
    def get_data_load(request, alumno_id):
        alumnoNombre = Alumnos.objects.get(id=alumno_id)
       # grupo=Grupos.objects.get(plan=alumnoNombre.plan)
        if Calificaciones.objects.filter(matricula=alumnoNombre.matricula).exists():
            list=Calificaciones.objects.filter(matricula=alumnoNombre.matricula)
        else:
            list=[]
        return render_to_response('reportes/Reporte_boleta_semestral.html',
                                  {'listado': list, 'alumno': alumnoNombre})
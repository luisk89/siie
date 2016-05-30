from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


from academica.views import PlanCreate, \
    PlanUpdate, ExtracurricularesCreate, GrupoCreate, GruposList, HorarioCreate, HorarioList, MateriaCreate, \
    MateriaList, MaestroCreate, MaestroList, CalificacionCreate, AlumnoCreate, AlumnoUpdate, \
    GrupoUpdate, CarreraCreate, CarreraList, AlumnoList, CicloSemestralCreate, CicloSemestralList, PlanEstudioList, \
    BajaCreate, CicloSemestralUpdate, CarreraUpdate, EncuestaCreate, \
    EncuestaList, ReinscripcionList, Home, EstadoCreate, EstadoList, MunicipioList, \
    MunicipioCreate, AulaCreate, AulaList, CalificacionList, ExtracurricularList, ServicioSocialCreate, \
    ServicioSocialList, ServicioLiberadosList, BecaCreate, BecaList, TipoBecaCreate, TipoBecaList, EscuelaCreate, \
    EscuelaList, BibliotecaCreate, BibliotecaList, CentroComputoCreate, CentroComputoList, ContabilidadCreate, \
    ContabilidadList, BajaBiblioteca, BibliotecaUpdate, BajaCC, CCUpdate, BajaConta, ContaUpdate, CalificacionesUpdate, \
    ServicioUpdate

__author__ = 'Luisk'

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', Home.as_view(), name='home'),
                       url(r'^deveploment/', TemplateView.as_view(template_name="404.html")),
                       # url(r'^list/$', AlumnosList.as_view(), name='alumnos-list'),
                       # planEstudio
                       url(r'planEstudio/add/$', PlanCreate.as_view(), name='planEstudio-add'),
                       url(r'planEstudio/(?P<pk>[0-9]+)/$', PlanUpdate.as_view(), name='planEstudio-update'),
                       url(r'planEstudio/list/$', PlanEstudioList.as_view(), name='list-planEstudio'),
                       # Alumno
                       url(r'alumno/add/$', AlumnoCreate.as_view(), name='alumno-add'),
                       url(r'alumno/(?P<pk>[0-9]+)/$', AlumnoUpdate.as_view(), name='alumno-update'),
                       url(r'alumno/list/$', AlumnoList.as_view(), name='list-alumno'),
                       url(r'^alumno/re/$', ReinscripcionList.as_view(), name='alumno-re'),
                       url(r'^alumno-ajax/$', ReinscripcionList.AlumnoAjax, name='alumno-ajax'),
                       # Extracurriculares
                       url(r'alumno/add/addExtracurricular/$', ExtracurricularesCreate.as_view(), name='extra-add'),
                       url(r'^extracurricular/list$', ExtracurricularList.as_view(), name='list-extra'),
                       # grupos
                       url(r'grupo/add/$', GrupoCreate.as_view(), name='grupo-add'),
                       url(r'grupo/list/$', GruposList.as_view(), name='list-grupos'),
                       url(r'grupo/(?P<pk>[0-9]+)/$', GrupoUpdate.as_view(), name='grupo-update'),
                       # horario
                       url(r'horario/add/$', HorarioCreate.as_view(), name='horario-add'),
                       url(r'horario/list/$', HorarioList.as_view(), name='list-horario'),
                       # materias
                       url(r'materia/add/$', MateriaCreate.as_view(), name='materia-add'),
                       url(r'materia/list/$', MateriaList.as_view(), name='list-materias'),
                       # maestros
                       url(r'maestro/add/$', MaestroCreate.as_view(), name='maestro-add'),
                       url(r'maestro/list/$', MaestroList.as_view(), name='list-maestro'),
                       # calificaciones
                       url(r'calificacion/add/$', CalificacionCreate.as_view(), name='calificacion-add'),
                       url(r'calificacion/list/$', CalificacionList.as_view(), name='list-calificacion'),
                       url(r'califAlum/(?P<alumno_id>\d+)/$', CalificacionList.get_calificacionesbyAlumno,
                           name='califi-alumno'),
                       url(r'myCalif/$', CalificacionList.get_my_calificaciones, name='my-califi'),
                       url(r'calificacion/update/(?P<pk>[0-9]+)/$', CalificacionesUpdate.as_view(), name='calificacion-update'),
                       # carrera
                       url(r'carrera/add/$', CarreraCreate.as_view(), name='carrera-add'),
                       url(r'carrera/list/$', CarreraList.as_view(), name='list-carrera'),
                       url(r'carrera/update/(?P<pk>[0-9]+)/$', CarreraUpdate.as_view(), name='carrera-update'),
                       # semestre
                       url(r'ciclosemestral/add/$', CicloSemestralCreate.as_view(), name='semestre-add'),
                       url(r'ciclosemestral/list/$', CicloSemestralList.as_view(), name='list-semestre'),
                       url(r'ciclosemestral/update/(?P<pk>[0-9]+)/$', CicloSemestralUpdate.as_view(),
                           name='semestre-update'),
                       url(r'^semestre-ajax/$', CicloSemestralList.SemestreAjax, name='semestre-ajax'),

                       url(r'baja/$', BajaCreate.as_view(), name='baja-add'),

                       url(r'biblioteca/add$', BibliotecaCreate.as_view(), name='biblio-add'),
                       url(r'biblioteca/list$', BibliotecaList.as_view(), name='list-biblio'),
                       url(r'biblioteca/delete$', BajaBiblioteca.as_view(), name='baja-biblio'),
                       url(r'biblioteca/(?P<pk>[0-9]+)/$', BibliotecaUpdate.as_view(), name='biblio-update'),

                       url(r'centrocomp/add$', CentroComputoCreate.as_view(), name='cc-add'),
                       url(r'centrocomp/list$', CentroComputoList.as_view(), name='list-cc'),
                       url(r'centrocomp/delete$', BajaCC.as_view(), name='baja-cc'),
                       url(r'centrocomp/(?P<pk>[0-9]+)/$', CCUpdate.as_view(), name='cc-update'),

                       url(r'contabilidad/add$', ContabilidadCreate.as_view(), name='conta-add'),
                       url(r'contabilidad/list$', ContabilidadList.as_view(), name='list-conta'),
                       url(r'centrocomp/delete$', BajaConta.as_view(), name='baja-cont'),
                       url(r'centrocomp/(?P<pk>[0-9]+)/$', ContaUpdate.as_view(), name='cont-update'),

                       url(r'encuesta/add/$', EncuestaCreate.as_view(), name='encuesta-add'),
                       url(r'encuesta/list/$', EncuestaList.as_view(), name='list-encuesta'),

                       url(r'estado/add/$', EstadoCreate.as_view(), name='estado-add'),
                       url(r'estado/list/$', EstadoList.as_view(), name='list-estado'),

                       url(r'municipio/add/$', MunicipioCreate.as_view(), name='municipio-add'),
                       url(r'municipio/list/$', MunicipioList.as_view(), name='list-municipio'),

                       url(r'aula/add/$', AulaCreate.as_view(), name='aula-add'),
                       url(r'aula/list/$', AulaList.as_view(), name='list-aula'),

                       url(r'servicio/add/$', ServicioSocialCreate.as_view(), name='servicio-add'),
                       url(r'servicio/list/$', ServicioSocialList.as_view(), name='list-servicio'),
                       url(r'serviciolib/list/$', ServicioLiberadosList.as_view(), name='list-servicioliberados'),
                       url(r'servicio/update/(?P<pk>[0-9]+)/$', ServicioUpdate.as_view(), name='servicio-update'),

                       url(r'beca/add/$', BecaCreate.as_view(), name='beca-add'),
                       url(r'beca/list/$', BecaList.as_view(), name='list-beca'),

                       url(r'tipob/add/$', TipoBecaCreate.as_view(), name='tbeca-add'),
                       url(r'tipob/list/$', TipoBecaList.as_view(), name='list-tbeca'),

                       url(r'escuela/add/$', EscuelaCreate.as_view(), name='escuela-add'),
                       url(r'escuela/list/$', EscuelaList.as_view(), name='list-escuela'),
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^admin/', include('manager.urls')),

                       ) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

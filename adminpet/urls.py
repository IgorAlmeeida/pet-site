from django.urls import path, include
from .views import ( home, 
                    listProjects, 
                    newProject, 
                    updateProject, 
                    deleteProject, 
                    listMyProjects, 
                    detailProject, 
                    newCronogramProject,
                    updateCronogramProject,
                    deleteCronogramProject,
                    listCronogramProject,
                    newActivityProject,
                    updateActivityProject,
                    deleteActivityProject,
                    listActivityProject)
                    
urlpatterns = [
    path('', home, name='page_home'),
    
    path('projeto/',listProjects, name='list_project'),
    path('projeto/my', listMyProjects, name='list_my_project'),
    path('projeto/new',newProject, name='new_project'),
    path('projeto/update/<int:id>/',updateProject,name='update_project'),
    path('projeto/delete/<int:id>/',deleteProject, name='delete_project'),
    path('projeto/detail/<int:id>/',detailProject, name='detail_project'),

    path('projeto/detail/<int:idProject>/cronograma/new',newCronogramProject, name='new_cronogram'),
    path('projeto/detail/<int:idProject>/cronograma/update/<idCronogram>/',updateCronogramProject, name='update_cronogram'),
    path('projeto/detail/<int:idProject>/cronograma/delete/<idCronogram>/',deleteCronogramProject, name='delete_cronogram'),
    path('projeto/detail/<int:idProject>/cronograma/list/',listCronogramProject, name='list_cronogram'),

    path('projeto/detail/<int:idProject>/atividade/new',newActivityProject, name='new_activity'),
    path('projeto/detail/<int:idProject>/atividade/update/<idActivity>/',updateActivityProject, name='update_activity'),
    path('projeto/detail/<int:idProject>/atividade/delete/<idActivity>/',deleteActivityProject, name='delete_activity'),
    path('projeto/detail/<int:idProject>/atividade/list/',listActivityProject, name='list_activity'),


]
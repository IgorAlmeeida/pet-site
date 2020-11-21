from django.urls import path, include
from .views import home, listProjects, newProject, updateProject, deleteProject, listMyProjects

urlpatterns = [
    path('', home, name='page_home'),
    path('projeto/',listProjects, name='list_project'),
    path('projeto/my', listMyProjects, name='list_my_project'),
    path('projeto/new',newProject, name='new_project'),
    path('projeto/update/<id>/',updateProject,name='update_project'),
    path('projeto/delete/<id>/',deleteProject, name='delete_project'),

]
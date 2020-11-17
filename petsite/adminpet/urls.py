from django.urls import path, include
from .views import home, list_projects, new_project, update_project, delete_project, list_my_projects

urlpatterns = [
    path('', home, name='page_home'),
    path('projeto/',list_projects, name='list_project'),
    path('projeto/my/', list_my_projects, name='list_my_project'),
    path('projeto/new',new_project, name='new_project'),
    path('projeto/update/<id>/',update_project,name='update_project'),
    path('projeto/delete/<id>/',delete_project, name='delete_project'),

]
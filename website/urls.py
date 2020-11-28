from django.urls import path, include

from .views import (home,
                    pageBlog,
                    pageMembers,
                    pageSelections,
                    pageContatus,
                    pagePost,
                    pageProject)
                                        
urlpatterns = [
    path('', home, name='page_home_website'),
    path('blog/', pageBlog, name='blog'),
    path('membros/', pageMembers, name='membros'),
    path('projeto/<int:idProjeto>', pageProject, name='projects'),
    path('selecoes/', pageSelections, name='selecoes'),
    path('contato/', pageContatus, name='contato'),
    path('post/<int:idPost>', pagePost, name='post'),
]
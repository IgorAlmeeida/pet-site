from django.urls import path, include

from .views import (home,
                    pageBlog,
                    pageMembers,
                    pageSelections,
                    pageBolsa,
                    pagePost,
                    pageProject,
                    cadastrarPessoa)
                                        
urlpatterns = [
    path('', home, name='page_home_website'),
    path('blog/', pageBlog, name='blog'),
    path('membros/', pageMembers, name='membros'),
    path('projeto/<int:idProject>', pageProject, name='projects'),
    path('selecoes/', pageSelections, name='selecoes'),
    path('bolsa/', pageBolsa, name='bolsa'),
    path('post/<int:idPost>', pagePost, name='post'),
    path('cadastarPessoa/', cadastrarPessoa, name='cadastrarPessoa'),
]
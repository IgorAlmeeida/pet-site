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
                    listActivityProject,
                    login,
                    forgotPassword,
                    register,
                    user_logout, 
                    deleteCategory,
                    newCategory,
                    updateCategory,
                    listCategory,
                    deletePost,
                    newPost,
                    detailPost,
                    listPost,
                    updatePost)
                    
urlpatterns = [
    path('', home, name='page_home'),
    path('login/', login, name='login'),
    path('logout/', user_logout,name='logout'),
    path('forgot_password/', forgotPassword, name='forgot_password'),
    path('register/', register, name='register'),
    
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

    path('blog/post/detail/<int:idPost>',detailPost, name='detail_post'),
    path('blog/post/new',newPost, name='new_post'),
    path('blog/post/update/<int:idPost>',updatePost, name='update_post'),
    path('blog/post/delete/<int:idPost>',deletePost, name='delete_post'),
    path('blog/post/list',listPost, name='list_post'),

    path('blog/categoria/new',newCategory, name='new_category'),
    path('blog/categoria/update/<int:idCategory>',updateCategory, name='update_category'),
    path('blog/categoria/delete/<int:idCategory>',deleteCategory, name='delete_category'),
    path('blog/categoria/list',listCategory, name='list_category'),





]
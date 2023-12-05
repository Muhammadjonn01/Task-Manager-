from django.urls import path
from .views import *


urlpatterns = [
     path('tasks/', ModelTaskDetail.as_view(), name = "alltasks"),
    path("", HomePageView.as_view() , name="homepage"),
    path("create/", TaskCreate.as_view() , name="create"),
    path("<int:pk>", TaskDetail.as_view(), name="task_detail"),
    path("<int:pk>/edit", EditTask.as_view(), name="task_edit"),
    path("<int:pk>/delete", DeleteTask.as_view(), name="task_delete"),
    
]

from django.urls import path
from app2.views import Home, Addstudent,DeleteStudent,UpdateStudent

urlpatterns = [
    path("",Home.as_view(),name='home'),
    path('add-student/',Addstudent.as_view(), name='add-student'),
    path('delete/',DeleteStudent.as_view(), name='delete'),
    path('update/<int:id>/',UpdateStudent.as_view(), name='update'),
]


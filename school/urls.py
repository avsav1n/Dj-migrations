from django.urls import path

from school.views import students_list, students_list2

urlpatterns = [
    path('', students_list, name='students'),
]

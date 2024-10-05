from random import randint, sample
from typing import Any
from django.core.management.base import BaseCommand
from django.db import models
from school.models import Teacher, Student

class Command(BaseCommand):
    help = 'Create m2m dependencies after migration'

    def handle(self, *args: Any, **options: Any) -> str | None:
        '''Команда заполнения базы данных m2m случайными связями после миграции
        '''
        teachers = Teacher.objects.all() 
        students = Student.objects.all()
        for teacher in teachers:
            students_quantity = randint(1, 3)
            student_for_teacher = sample(list(students), students_quantity)
            teacher.students.add(*student_for_teacher)

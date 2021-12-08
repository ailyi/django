from django.shortcuts import render

from students.forms import CreateStudentForm
from students.models import StudentModel


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_average_grade(self):
        summa = sum(self.grades)
        return summa / len(self.grades)


def add_student(request):
    form = CreateStudentForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            grades_text = form.cleaned_data['grades']
            student = Student(
                name=form.cleaned_data['name'],
                grades=list(map(int, grades_text.split(',')))
            )
            student_model = StudentModel(
                name=student.name,
                grades=grades_text,
                average_grade=student.get_average_grade()
            )

            student_model.save()

            context = {
                'student': student_model,
            }

            return render(
                request,
                template_name='student.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_student.html',
        context=context,
    )


def show_student(request, id):
    context = {
        'student': StudentModel.objects.get(id=id),
    }

    return render(
        request,
        template_name='student.html',
        context=context,
    )


def show_students(request):
    students = StudentModel.objects.all()
    return render(
        request,
        template_name='students.html',
        context={'students': students}
    )

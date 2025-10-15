from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
# from .forms import StudentForm

# Home page view
def home(request):
    return render(request, 'home.html')

# View all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add a new student
from .models import Student

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        date_joined = request.POST.get('date_joined')

        if name and email and phone and course and date_joined:
            Student.objects.create(
                name=name,
                email=email,
                phone=phone,
                course=course,
                date_joined=date_joined
            )
            return redirect('student_list')
    return render(request, 'add_student.html')


# Edit an existing student
from django.shortcuts import get_object_or_404

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.course = request.POST.get('course')
        student.date_joined = request.POST.get('date_joined')
        student.save()
        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})


# Delete a student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')

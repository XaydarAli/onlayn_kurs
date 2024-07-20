from django.shortcuts import render, redirect,get_object_or_404
from .models import Course, Speciality,Teacher
from .forms import CourseForm,CourseUpdateForm,TeacherForm,TeacherUpdateForm,SpecialityUpdateForm,SpecialityForm

def courses_list_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    context = {
        "courses": courses,
        "specialitys": specialitys,
    }
    return render(request, 'course.html', context)


def course_detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_detail.html', {"course": course})


def course_create_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-list')
        else:
            return render(request, 'course_create.html', {'form': form, "message_error": "Qayerdadur xatolik mavjud!"})

    form = CourseForm()
    return render(request, 'course_create.html', {'form': form})

def course_update_view(request,pk):
    course=get_object_or_404(Course,pk=pk)
    if request.method == "POST":
        form=CourseUpdateForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-detail',pk=course.pk)
        else:
            form=CourseUpdateForm(instance=course)
    course = Course.objects.get(pk=pk)
    return render(request,'course_update.html',{"course":course})
def course_delete_view(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course-list')
    return render(request, 'course_create.html', {'form': form})


#****************************************************************************************************
def teachers_list_view(request):
    teachers = Teacher.objects.all()
    specialitys = Speciality.objects.all()
    return render(request, 'teacher.html',{"teachers":teachers})


def teacher_detail_view(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'teacher_detail.html', {"teacher": teacher})


def teacher_create_view(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')
        else:
            return render(request, 'teacher_create.html', {'form': form, "message_error": "Qayerdadur xatolik mavjud!"})

    form = TeacherForm()
    return render(request, 'teacher_create.html', {'form': form})

def teacher_update_view(request,id):
    teacher=get_object_or_404(Teacher,id=id)
    if request.method == "POST":
        form=TeacherUpdateForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher-detail',id=teacher.id)
        else:
            form=TeacherUpdateForm(instance=teacher)
    teacher = Teacher.objects.get(id=id)
    return render(request,'teacher_update.html',{"teacher":teacher})
def teacher_delete_view(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('teacher-list')
    return render(request, 'teacher_create.html', {'form': form})




#**********************************************************************************************************************************8
def speciality_list_view(request):
    specialitys = Speciality.objects.all()
    context = {
        "specialitys": specialitys,
    }
    return render(request, 'speciality.html', context)


def speciality_detail_view(request, id):
    speciality = Speciality.objects.get(id=id)
    return render(request, 'speciality_detail.html', {"speciality": speciality})


def speciality_create_view(request):
    if request.method == "POST":
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('speciality-list')
        else:
            return render(request, 'speciality_create.html', {'form': form, "message_error": "there is a mistake somewhere!"})

    form = SpecialityForm()
    return render(request, 'speciality_create.html', {'form': form})

def speciality_update_view(request,id):
    speciality=get_object_or_404(Speciality,id=id)
    if request.method == "POST":
        form=SpecialityUpdateForm(request.POST,instance=speciality)
        if form.is_valid():
            form.save()
            return redirect('speciality-detail',id=speciality.id)
        else:
            form=SpecialityUpdateForm(instance=speciality)
    speciality = Speciality.objects.get(id=id)
    return render(request,'speciality_update.html',{"speciality":speciality})
def speciality_delete_view(request, id):
    speciality = Speciality.objects.get(id=id)
    speciality.delete()
    return redirect('speciality-list')
    return render(request, 'speciality_create.html', {'form': form})







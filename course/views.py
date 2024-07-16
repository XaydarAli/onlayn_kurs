from django.shortcuts import render, redirect
from .models import Course, Speciality
from .forms import CourseForm


def courses_list_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    context = {
        "courses": courses,
        "specialitys": specialitys,
    }
    return render(request, 'course.html', context)


def course_detail_view(request, id):
    course = Course.objects.get(id=id)
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


def course_delete_view(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course-list')
    return render(request, 'course_create.html', {'form': form})

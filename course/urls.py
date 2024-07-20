from django.urls import path
from .views import courses_list_view, course_create_view, course_detail_view, course_delete_view,course_update_view
from .views import teachers_list_view, teacher_create_view, teacher_detail_view, teacher_delete_view,teacher_update_view
from .views import speciality_list_view, speciality_create_view, speciality_detail_view, speciality_delete_view,speciality_update_view

urlpatterns = [
    path('course/', courses_list_view, name='course-list'),
    path('course/create/', course_create_view, name='course-create'),
    path('course/<int:pk>/', course_detail_view, name='course-detail'),
    path('course//<int:id>/delete/', course_delete_view, name='course-delete'),
    path('course//<int:pk>/update/', course_update_view, name='course-update'),

    path('teacher/', teachers_list_view, name='teacher-list'),
    path('teacher/create/', teacher_create_view, name='teacher-create'),
    path('teacher/<int:id>/', teacher_detail_view, name='teacher-detail'),
    path('teacher//<int:id>/delete/', teacher_delete_view, name='teacher-delete'),
    path('teacher//<int:id>/update/', teacher_update_view, name='teacher-update'),


    path('speciality/', speciality_list_view, name='speciality-list'),
    path('speciality/create/', speciality_create_view, name='speciality-create'),
    path('speciality/<int:id>/', speciality_detail_view, name='speciality-detail'),
    path('speciality//<int:id>/delete/', speciality_delete_view, name='speciality-delete'),
    path('speciality//<int:id>/update/', speciality_update_view, name='speciality-update'),

]
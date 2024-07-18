from django.urls import path
from .views import courses_list_view, course_create_view, course_detail_view, course_delete_view,course_update_view
from .views import teachers_list_view, teacher_create_view, teacher_detail_view, teacher_delete_view,teacher_update_view

urlpatterns = [
    path('course/', courses_list_view, name='course-list'),
    path('course/create/', course_create_view, name='course-create'),
    path('course/<int:pk>/', course_detail_view, name='course-detail'),
    path('course//<int:id>/delete/', course_delete_view, name='course-delete'),
    path('course//<int:pk>/update/', course_update_view, name='course-update'),

    path('teacher/', teachers_list_view, name='teacher-list'),
    path('teacher/create/', teacher_create_view, name='teacher-create'),
    path('teacher/<int:pk>/', teacher_detail_view, name='teacher-detail'),
    path('teacher//<int:id>/delete/', teacher_delete_view, name='teacher-delete'),
    path('teacher//<int:pk>/update/', teacher_update_view, name='teacher-update'),

]
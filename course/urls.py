from django.urls import path
from .views import courses_list_view, course_create_view, course_detail_view, course_delete_view

urlpatterns = [
    path('course/', courses_list_view, name='course-list'),
    path('course/create/', course_create_view, name='course-create'),
    path('course/<int:id>/', course_detail_view, name='course-detail'),
    path('course/delete/<int:id>/', course_delete_view, name='course-delete'),
]
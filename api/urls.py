from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import student_list_create, StudentDetailView, TeacherViewset, CourseListCreateView, CourseUpdateDeleteView

router = DefaultRouter()

router.register(r"teachers", TeacherViewset)

urlpatterns = [
    path('students/', student_list_create, name= "student-list-create"),
    path('students/<int:pk>/', StudentDetailView.as_view(), name= "student-detail"),
    path('courses/', CourseListCreateView.as_view(), name= "course-list-create"),
    path('course/<int:pk>/', CourseUpdateDeleteView.as_view(), name= "course-update-delete"),
    path('', include(router.urls)), 
]
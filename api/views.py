from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins, generics, status
from .models import Student, Teacher, Course
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer


## Planning to use all types of views for my understanding

""" Here we are using Function based Views: to get and show all the students in the database"""

@api_view(["GET", "POST"])
def student_list_create(request):
    if request.method == "GET":
        students = Student.objects.all()
        serialzer = StudentSerializer(students, many=True)

        return Response(serialzer.data)

    elif request.method == "POST":
        serialzer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()

            return Response(serialzer.data, status=status.HTTP_201_CREATED)

        return Response(serialzer.errors)


""" Here we are using Student in detail(we will be taking the "id" which is a primary key) view using Class Based View """

class StudentDetailView(APIView):
    def get(self, request, pk):
        student = get_object_or_404(
            Student, pk=pk
        )  ##we can also use this """student = Student.objects.get(pk=pk)"""
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Here we are using Viewsets which will make our operations much easier and minimal code """

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



"""Here we are using GENERICS """
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


"""Here we will be using MIXINS """

class CourseUpdateDeleteView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializer 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


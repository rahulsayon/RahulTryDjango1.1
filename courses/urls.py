
from django.contrib import admin
from django.urls import path
from courses.views import CourseView,CourseListView,CourseCreateView,CourseUpdateView,CourseDeleteView,sendemail



urlpatterns = [
path('' , CourseListView.as_view()  , name="course-list"),
path('<int:id>/' , CourseView.as_view()  , name="course-details"),
path('create/' , CourseCreateView.as_view()  , name="course-create"),
path('<int:id>/update/' , CourseUpdateView.as_view()  , name="course-update"),
path('<int:id>/delete/' , CourseDeleteView.as_view()  , name="course-delete"),
path('send/' , sendemail  , name="send"),

]
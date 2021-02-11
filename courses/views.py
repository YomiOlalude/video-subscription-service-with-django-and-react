from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Lesson

# Create your views here.


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
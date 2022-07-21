from multiprocessing.spawn import import_main_path
from rest_framework import generics
from ..models import Subject, Course
from .serializers import SubjectSerializer
from courses.api import serializers


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



from django.shortcuts import render
from rest_framework import viewsets
from UPortalApp.serializer import *
from UPortalApp.models import *
from django.shortcuts import render

def main(request):

    return render(request, 'index.html')

# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PlaceOPViewSet(viewsets.ModelViewSet):
    queryset = Place_of_publication.objects.all()
    serializer_class = PlaceOPSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PlaceOPSerializer


class AuthorOPViewSet(viewsets.ModelViewSet):
    queryset = Author_of_publication.objects.all()
    serializer_class = AuthorOPSerializer
from UPortalApp.models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('nameRus', 'nameEng')

class PlaceOPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place_of_publication
        fields = ('name', 'type_of_place', 'publishing_house', 'place_of_publish', 'description', 'list_of_links')

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ('title', 'date_of_publication', 'language_of_publication', 'description', 'type_of_publication', 'type_of_index',
                  'place_of_publication', 'pages', 'links')

class AuthorOPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author_of_publication
        fields = ('author', 'publication')

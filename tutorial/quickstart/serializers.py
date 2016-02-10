from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import Author, Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
"""
class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('url', 'record_name') """
        
class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn')
        
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    books = BookSerializer(many=True) 
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')
        
        
       
               

from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from tutorial.quickstart.models import Author, Book
from talk.models import Post


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
        

        
"""        
    # http://code.tutsplus.com/tutorials/beginners-guide-to-the-django-rest-framework--cms-19786    
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn')
        
class AuthorSerializer(serializers.ModelSerializer):
    
    books = BookSerializer(many=True) 
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')
        """
        
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created', 'updated')
        
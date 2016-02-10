from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group, Author
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer,AuthorSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
"""    
class RecordViewSet(viewsets.ModelViewSet):
    
    #API endpoint that allows groups to be viewed or edited.
    
    queryset = Record.objects.all()
    serializer_class = RecordSerializer  """
      
    
class AuthorView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Author
    serializer_class = AuthorSerializer
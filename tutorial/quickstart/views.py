from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from talk.models import Post
from talk.serializers import PostSerializer
from talk.forms import PostForm


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'talk/index.html', tmpl_vars)


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_element(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

# Previous code

"""
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer,AuthorSerializer
from tutorial.quickstart.models import Author, Book


class UserViewSet(viewsets.ModelViewSet):
    
    #API endpoint that allows users to be viewed or edited.
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    
    #API endpoint that allows groups to be viewed or edited.
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class AuthorView(generics.ListAPIView):

    #Returns a list of all authors.
    
    model = Author
    serializer_class = AuthorSerializer   
    """
    
"""    
class RecordViewSet(viewsets.ModelViewSet):
    
    #API endpoint that allows groups to be viewed or edited.
    
    queryset = Record.objects.all()
    serializer_class = RecordSerializer  """
      
    

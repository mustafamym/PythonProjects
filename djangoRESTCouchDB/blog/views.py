from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from blog.models import BlogPost, SERVER
from blog.serializers import BlogPostSerializer


db = SERVER['blogs']

@api_view(['POST'])
def create_blog(request):
    """Take JSON post and create BlogPost record"""
    data = JSONParser().parse(request)

    serializer = BlogPostSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['GET'])
def blog_detail(request, blog_post_id):
    """Show details for given paper"""
    blogpost = BlogPost.load(db, blog_post_id)
    serializer = BlogPostSerializer(blogpost)
    return Response(serializer.data)

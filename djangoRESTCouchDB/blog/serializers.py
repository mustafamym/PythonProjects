"""
Simple serializer setup for blog bolgs.

This is a simple demo based on the tutorial at:
http://www.django-rest-framework.org/api-guide/serializers/#modelserializer
"""
from rest_framework import serializers
from blog.models import BlogPost, SERVER

db = SERVER['blogs']

class BlogPostSerializer(serializers.Serializer):
    """Basic serializer for papers"""

    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    abstract = serializers.CharField()
    type = serializers.CharField()

    # you can specify validate function for field xyz using validate_xyz
    def validate_type(self, value):
        """Document type must be one of a set list of allowed values."""
        if value not in ['proceedings', 'shortpaper', 'journal']:
            raise serializers.ValidationError("BlogPost type must be valid")
        else:
            return value

    def create(self, validated_data):
        """Create a blogpost from scratch"""

        blogpost = BlogPost()
        return self.update(blogpost, validated_data)

    def update(self, blogpost, validated_data):
        """Merge an existing document with validated data"""

        blogpost.title = validated_data.get('title')
        blogpost.abstract = validated_data.get('abstract')
        blogpost.type = validated_data.get('type')
        blogpost.store(db)

        return blogpost

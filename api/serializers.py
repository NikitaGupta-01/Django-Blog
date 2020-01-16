from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['title', 'content', 'date_posted']
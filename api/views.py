from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorator import api_view

from users.models import Profile
from blog.models import Post
from blog.api.serializers import PostSerializer
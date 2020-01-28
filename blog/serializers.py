from rest_framework import serializers
from blog.models import	Post

# class PostSerializer(serializers.Serializer):
# 	title = serializers.CharField(read_only=True)
# 	content = serializers.CharField(required=False, allow_blank=True, max_length=100)
# 	date_posted = serializers.DateTimeField(read_only=True)

# 	# author = serializers.ForeignKey(User , on_delete=models.CASCADE ,null=False, blank=False)

# 	def create(self, validated_data):
# 		return Update.objects.create(**validated_data)
# 		#Create and return a new `Snippet` instance, given the validated data.


# 	def update(self,instance,validated_data):
# 		instance.title = validated_data.get('title',instance.title)
# 		instance.content = validated_data.get('content',instance.content)
# 		instance.save()
# 		return instance
	
		
	
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'author']
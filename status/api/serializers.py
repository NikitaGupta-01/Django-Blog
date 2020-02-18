from rest_framework import serializers
from status.models import Status

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Status
		fields 	= ['id','user','content']

	# def validate_<fieldname>(self,value):    field level validation 
	# def validate_content(self,value):
	# 	if(len(value)>100):
	# 		raise ValidationError("this is long")
	# 	return value


	def validate(self,data):    #take raw data whole validation
		content=data.get("content",None)
		if(content ==""):
			content=None
		if content is None:
			raise serializers.ValidationError("content or image is required")
		return data

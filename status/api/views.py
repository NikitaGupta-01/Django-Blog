from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import StatusSerializer
from status.models import Status
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins


class StatusAPIView(generics.ListAPIView, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):    #we'll be using list view bcz at the end we will get a list of items
	permission_classes 		= []
	authentication_classes 	= []
	# queryset				= Status.objects.all()
	serializer_class		= StatusSerializer

	def get_queryset(self):
		request		= self.request
		qs 		= Status.objects.all()
		query 	= request.GET.get('q')
		if query is not None:
			qs = qs.filter(content__icontains = query)
		return qs


	def get_object(self):     #for detail view
		request		= self.request
		passed_id	= request.GET.get('id')
		queryset 	= self.get_queryset()
		obj 		= None
		if passed_id is not None:
			obj 	= get_object_or_404(queryset,id=passed_id)
			self.check_object_permissions(request,obj)
		return obj

# to overwrite get method for ListAPIview

	def get(self,request,*args,**kwargs):
		passed_id	= request.GET.get('id')
		# request.data
		# request.body
		if passed_id is not None:
			return self.retrieve(request,*args,**kwargs)           
		return super().get(request,*args,**kwargs)
		

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)

	# def perform_create(self,serializer):    
	# 	serilizer.save(user=self.request.user)






# class StatusSearchAPIView(APIView):
# 	permission_classes 		= []
# 	authentication_classes 	= []

# 	def get(self,request,format=None):
# 		qs=Status.objects.all()
# 		serializer=StatusSerializer(qs,many=True)
# 		return Response(serializer.data)  #qs is no iterable hence we need to serialize

# 	def post(self,request,format=None):
# 		qs=Status.objects.all()
# 		serializer=StatusSerializer(qs,many=True)
# 		return Response(serializer.data) 


# class StatusAPIView(generics.ListAPIView, mixins.CreateModelMixin):
# 	permission_classes 		= []
# 	authentication_classes 	= []
# 	# queryset				= Status.objects.all()
# 	serializer_class		= StatusSerializer

# 	def get_queryset(self):
# 		qs 		= Status.objects.all()
# 		query 	= self.request.GET.get('q')
# 		if query is not None:
# 			qs = qs.filter(content__icontains = query)
# 		return qs

# 	def post(self,*args,**kwargs):
# 		return self.create(request,*args,**kwargs)

# 		#works same for mixin too
# 	# def perform_create(self,serializer):    # not serrializer class but one declared above is used
# 	# 	serilizer.save(user=self.request.user)



# # class StatusCreateAPIView(generics.CreateAPIView):   same work done by mixin on same page
# # 	permission_classes 		= []
# # 	authentication_classes 	= []
# # 	queryset				= Status.objects.all()
# # 	serializer_class		= StatusSerializer

# 	# def perform_create(self,serializer):    # not serrializer class but one declared above is used
# 	# 	serilizer.save(user=self.request.user)




# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  #similar to below StatusDetailAPIView but more compact and cleaner
# 	permission_classes 		= []
# 	authentication_classes 	= []
# 	queryset				= Status.objects.all()
# 	serializer_class		= StatusSerializer
# 	lookup_field 			= 'id'



# # class StatusDetailAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
# # 	permission_classes 		= []
# # 	authentication_classes 	= []
# # 	queryset				= Status.objects.all()
# # 	serializer_class		= StatusSerializer
# # 	lookup_field 			= 'id'

# # 	def put(self,*args,**kwargs):
# # 		return self.update(request,*args,**kwargs)
# #	def put(self,*args,**kwargs):
# # 		return self.update(request,*args,**kwargs)
# # 	def delete(self,*args,**kwargs):
# # 		return self.destroy(request,*args,**kwargs)

# 	# def get_object(self,*args,**kwargs):     #similar to loopkup_field use any one
# 	# 	kwargs	= self.kwargs
# 	# 	kw_id	= kwargs.get('id')
# 	# 	return Status.objects.get(id=kw_id)
	


# # class StatusUpdateAPIView(generics.UpdateAPIView):
# # 	permission_classes 		= []
# # 	authentication_classes 	= []
# # 	queryset				= Status.objects.all()
# # 	serializer_class		= StatusSerializer


# # class StatusDeleteAPIView(generics.DestroyAPIView):
# # 	permission_classes 		= []
# # 	authentication_classes 	= []
# # 	queryset				= Status.objects.all()
# # 	serializer_class		= StatusSerializer
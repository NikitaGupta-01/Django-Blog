from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm ,  UserUpdateForm, ProfileUpdateForm 


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from users.models import Profile
from users.serializers import ProfileSerializer


def register(request):
	if request.method =='POST':
		form = 	UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request , f'Account created succesfully. Log In!')
			return redirect('login')	
	else:
		form = 	UserRegisterForm()
	return render(request , 'users/register.html' , {'form' : form})



@login_required
def profile(request):
	if request.method == 'POST':
		p_form = ProfileUpdateForm(request.POST , instance = request.user.profile)
		u_form = UserUpdateForm(request.POST , request.FILES , instance = request.user)
		if u_form.is_valid() and p_form.is_valid():
			p_form.save()
			u_form.save()
			messages.success(request , f'Updated succesfully!')
			return redirect('profile')	
	else:
		p_form = ProfileUpdateForm(instance = request.user.profile)
		u_form = UserUpdateForm(instance = request.user)
	
	context = {
	'p_form': p_form ,
	'u_form': u_form
	}
	return render(request , 'users/profile.html' , context)


@csrf_exempt
def snippet_list(request):
    #List all code snippets, or create a new snippet.
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
from django.contrib import admin
from .models import Status
from .forms import StatusForms


class StatusAdmin(admin.ModelAdmin):
	list_display	= ['user','content']
	form 			= StatusForms

admin.site.register(Status,StatusAdmin)




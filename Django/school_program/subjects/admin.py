from django.contrib import admin
from .models import Subject

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name','score')
    search_fields = ('subject_name','score')

# allow display on admin page
admin.site.register(Subject, SubjectAdmin)
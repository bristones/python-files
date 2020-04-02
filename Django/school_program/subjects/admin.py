from django.contrib import admin
from .models import Subject

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name','score','student')
    search_fields = ('subject_name','score','student__name')

# allow display on admin page
admin.site.register(Subject, SubjectAdmin)
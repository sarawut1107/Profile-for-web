from resume.models import resume
from django.contrib import admin
from .models import comment, resume
# Register your models here.
class resumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    search_fields = ('title',)

# Register your models here.
class commentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    search_fields = ('title',)

admin.site.register(resume, resumeAdmin)
admin.site.register(comment, commentAdmin)
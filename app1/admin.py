from django.contrib import admin

# Register your models here.
from app1.models import Student
class std_admin(admin.ModelAdmin):
    list_display=['name','age','course']
admin.site.register(Student,std_admin)

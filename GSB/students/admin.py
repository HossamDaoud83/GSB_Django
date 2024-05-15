from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(StudentsTbl)
class StudentsTblAdmin(admin.ModelAdmin):
    list_display = ('id', 'engname', 'arabicname', 'regno', 'program', 'term', 'phone', 'status', 'email',
                    'studylocation', 'intakesemester')
    list_display_links = ('id', 'engname', 'regno')
    list_per_page = 25
    search_fields = ['engname', 'arabicname', 'regno', 'phone', 'email']
    ordering = ['engname', 'arabicname']

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

@admin.register(Categorylist)
class CategorylistAdmin(admin.ModelAdmin):
    list_display = ('idcategory', 'category')

@admin.register(Collegelist)
class CollegelistAdmin(admin.ModelAdmin):
    list_display = ('collegeid', 'college')

@admin.register(Majorlist)
class MajorlistAdmin(admin.ModelAdmin):
    list_display = ('majorid', 'group')

@admin.register(Nationalitylist)
class NationalitylistAdmin(admin.ModelAdmin):
    list_display = ('nationalid', 'nationality')
    ordering = ['nationality']

@admin.register(Programlist)
class ProgramlistAdmin(admin.ModelAdmin):
    list_display = ('programid', 'programname')
    ordering = ['programname']

@admin.register(Studentaffairslist)
class StudentaffairslistAdmin(admin.ModelAdmin):
    list_display = ('employeesid', 'studentaffairs')
    ordering = ['studentaffairs']

@admin.register(Tblcitylist)
class TblcitylistAdmin(admin.ModelAdmin):
    list_display = ('citylistid', 'cityname')
    ordering = ['cityname']

@admin.register(Tblsemesterslist)
class TblsemesterslistAdmin(admin.ModelAdmin):
    list_display = ('id', 'semester')
    ordering = ['semester']

@admin.register(Tblsubjectslist)
class TblsubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'subjectname','subjectcode','program')
    ordering = ['subjectname']

@admin.register(Tblstatuslist)
class TblstatuslistAdmin(admin.ModelAdmin):
    list_display = ('id', 'statuslist')
    ordering = ['statuslist']
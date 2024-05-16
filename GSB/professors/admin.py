from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Tblcontacts)
class TblcontactsAdmin(admin.ModelAdmin):
    list_display = ('contactsid', 'aastid', 'atitle', 'aname', 'etitle', 'ename', 'esurname', 'asurname', 'email1',
                    'phone1', 'academicdegree', 'paymentdegree', 'contreply', 'delvexam', 'delvresults', 'otherfess',
                    'totalfees', 'moodle_user', 'ms_teams_user')
    list_display_links = ('contactsid', 'esurname')
    list_per_page = 25
    search_fields = ['phone1', 'esurname', 'asurname', 'email1']
    ordering = ['esurname', 'asurname']


@admin.register(Tblcategorylist)
class TblcategorylistAdmin(admin.ModelAdmin):
    list_display = ('categorylistid', 'categoryname')
    ordering = ['categoryname']


@admin.register(Tblcitylist)
class TblcitylistAdmin(admin.ModelAdmin):
    list_display = ('citylistid', 'cityname')
    ordering = ['cityname']

@admin.register(Tbleducode)
class TbleducodeAdmin(admin.ModelAdmin):
    list_display = ('educode',)
    ordering = ['educode']

@admin.register(Tblmajorlist)
class TblmajorlistAdmin(admin.ModelAdmin):
    list_display = ('majorlistid', 'majorname')
    ordering = ['majorname']

@admin.register(Tblprogramlist)
class TblprogramlistAdmin(admin.ModelAdmin):
    list_display = ('programlistid', 'programname')
    ordering = ['programname']

@admin.register(Tblsemesterlist)
class TblsemesterAdmin(admin.ModelAdmin):
    list_display = ('semesterlistid', 'semestername')
    ordering = ['semestername']

@admin.register(Tblsubjectslist)
class TblsubjectsAdmin(admin.ModelAdmin):
    list_display = ('subjectid', 'subjectcode', 'subjectname', 'type','program', 'major_name')
    ordering = ['subjectname']

@admin.register(Tbltimetabletypelist)
class TbltimetabletypelistAdmin(admin.ModelAdmin):
    list_display = ('idtimetabletype', 'timetabletype')
    ordering = ['timetabletype']
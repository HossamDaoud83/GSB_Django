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
